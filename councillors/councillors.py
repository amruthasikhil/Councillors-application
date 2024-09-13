from flask import Flask, render_template, request, session, jsonify, redirect
import demjson
from DBConnection import Db
import datetime
import random
db=Db()
app = Flask(__name__)
app.secret_key="nnn"
# admin-----------------------------------------------------------------------------------------------------------------
@app.route('/')
def hello_world():
    return render_template("login.html")
@app.route('/admin')
def admin():
    b = session['type']
    print(b)
    if b=="admin":
        if session['lg'] == "lin":
            return render_template("admin/index.html")
        else:
            return render_template("login.html")
    else:
        return render_template('/login.html')
@app.route('/may')
def may():
    b = session['type']
    print(b)
    if b=="mayor":
        if session['lg'] == "lin":
            return render_template("mayor/index.html")
        else:
            return render_template("login.html")
    else:
        return render_template('/login.html')
@app.route('/councillor_home')
def councillors_home():
    b = session['type']
    print(b)
    if b == "councillors":
        if session['lg'] == "lin":
            return render_template("councillor/index.html")
        else:
            return render_template("login.html")
    else:
        return render_template('/login.html')

@app.route('/clerk_home')
def clerk_home():
    b = session['type']
    print(b)
    if b == "clerks":
        if session['lg'] == "lin":
            return render_template("clerk/index.html")
        else:
            return render_template("login.html")
    else:
        return render_template('/login.html')
@app.route('/dept_home')
def dept_home():
    b = session['type']
    print(b)
    if b == "dept":
        if session['lg'] == "lin":
            return render_template("dept/index.html")
        else:
            return render_template("login.html")
    else:
        return render_template('/login.html')

@app.route('/login',methods=['post','get'])
def login():
    if request.method == "POST":
        uname = request.form['textfield']
        password = request.form['textfield2']

        q1 = "select * from logintable where username='" + uname + "' and password='" + password + "'"
        res = db.select(q1)
        if len(res) > 0:
            type = res[0]['usertype']
            print(type)
            session['type'] = type
            b=session['type']
            if type is not None:
                if type == "admin":
                    session['login_id'] = res[0]['login_id']
                    a = session['login_id']
                    session['lg'] = "lin"
                    print(a)
                    return redirect('/admin')


                elif type == "mayor":
                    session['login_id'] = res[0]['login_id']
                    a = session['login_id']
                    session['lg'] = "lin"
                    print(a)
                    return redirect('/may')
                elif type == "councillors":
                    session['login_id'] = res[0]['login_id']
                    a = session['login_id']
                    q2="select * from councillor where login_id='"+str(a)+"'"
                    res1=db.selectOne(q2)
                    session['ward'] = res1['ward']
                    a1=session['ward']
                    print(a1)
                    a = session['login_id']
                    session['lg'] = "lin"
                    print(a)
                    return redirect("/councillor_home")
                elif type == "clerks":
                    session['login_id'] = res[0]['login_id']
                    a = session['login_id']
                    session['lg'] = "lin"
                    print(a)
                    return redirect("/clerk_home")

                elif type == "dept":
                    session['login_id'] = res[0]['login_id']
                    a = session['login_id']
                    session['lg'] = "lin"
                    return redirect('/dept_home')

                else:
                    return "error"
            else:
                return "error"

        else:
            return "error"
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session['lg']=""
    # return render_template("admin/inbox.html")
    return render_template("login.html")

@app.route('/admin_home')
def admin_home():
    if session['lg'] == "lin":
        return render_template("admin/adminhome.html")
    else:
        return  render_template("login.html")

#mayor mgt------------------------------------
@app.route('/admin_add_mayor')
def admin_add_mayor():
    if session['lg'] == "lin":
        return render_template("admin/addmayor.html")
    else:
        return  render_template("login.html")

@app.route('/addmayor',methods=['post'])
def addmayor():
    if session['lg']=="lin":
        name=request.form['name']
        gender=request.form['gender']
        dob=request.form['dob']
        house_name=request.form['hn']
        place=request.form['place']
        ph=request.form['ph']
        pin=request.form['pin']
        dis=request.form['dis']
        email=request.form['email']
        pic=request.files['pic']
        password=random.randint(0000,9999)
        data = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        pic.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\mayor\\" + data + ".jpg")
        path = "/static/mayor/" + data + ".jpg"
        print(path)
        q3="select mayor.*,logintable.* from logintable inner join mayor on mayor.login_id=logintable.login_id where logintable.usertype='mayor'"
        res3=db.select(q3)
        print("jjjjjjjj")
        if res3 is  None:
            print("mmmmmmmm")
            q2="insert into logintable(username,password,usertype)values('"+email+"','"+str(password)+"','mayor')"
            res=db.insert(q2)
            print(res)
            q1="insert into mayor(mayor_name,picture,email,gender,dob,house_name,place,pincode,login_id,phone,district,joindate,enddate) values('"+name+"','"+path+"','"+email+"','"+gender+"','"+dob+"','"+house_name+"','"+place+"','"+pin+"','"+str(res)+"','"+ph+"','"+dis+"',curdate(),date_add(curdate(),interval 1825 day))"
            res1=db.insert(q1)
            return admin_add_mayor()
        else:
            print("elsssssssssss")
            return '<script>alert("cannot added......");window.location="/admin_add_mayor"</script>'
    else:
        return render_template("login.html")
@app.route('/admin_view_mayor')
def admin_view_mayor():
    if session['lg'] == "lin":
        q3="select logintable.*,mayor.* from mayor inner join logintable on logintable.login_id=mayor.login_id where logintable.usertype='mayor'"
        res=db.select(q3)
        return render_template("admin/viewmayor.html",data=res)
    else:
        return render_template("login.html")

@app.route('/mayor_update/<i>')
def mayor_update(i):
    if session['lg'] == "lin":
        q4="select * from mayor where mayor_id='"+i+"'"
        res=db.selectOne(q4)
        print(res)
        return render_template("admin/updatemayor.html",data=res)
    else:
        return render_template("login.html")
@app.route('/update',methods=['post'])
def update():
    if session['lg'] == "lin":
        mid=request.form['id1']
        name = request.form['name']
        gender = request.form['gender']
        dob = request.form['dob']
        house_name = request.form['hn']
        place = request.form['place']
        ph = request.form['ph']
        pin = request.form['pin']
        dis = request.form['dis']
        # email = request.form['email']
        pic = request.files['pic']
        # print(pic)

        # print(data)
        if request.files is not None:
            if pic.filename != "":
                data = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                pic.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\mayor\\" + data + ".jpg")
                path = "/static/mayor/" + data + ".jpg"
                q4 = "update mayor set mayor_name='" + name + "',picture='" + path + "',gender='" + gender + "',dob='" + dob + "',house_name='" + house_name + "',place='" + place + "',pincode='" + pin + "',phone='" + ph + "',district='" + dis + "' where mayor_id='" + str(mid) + "'"
                res = db.update(q4)
                return admin_view_mayor()

            else:
                 q5 = "update mayor set mayor_name='" + name + "',gender='" + gender + "',dob='" + dob + "',house_name='" + house_name + "',place='" + place + "',pincode='" + pin + "',phone='" + ph + "',district='" + dis + "' where mayor_id='" + str(mid) + "'"
                 res = db.update(q5)
                 return admin_view_mayor()
        else:
            q5 = "update mayor set mayor_name='" + name + "',gender='" + gender + "',dob='" + dob + "',house_name='" + house_name + "',place='" + place + "',pincode='" + pin + "',phone='" + ph + "',district='" + dis + "' where mayor_id='" + str(mid) + "'"
            res = db.update(q5)
            return admin_view_mayor()
    else:
        return render_template("login.html")

@app.route('/mayor_delete/<i>')
def mayor_delete(i):
    if session['lg'] == "lin":
        q4="update logintable set usertype='blocked' where login_id='"+str(i)+"'"
        res=db.update(q4)
        return admin_view_mayor()
    else:
        return render_template("login.html")
@app.route('/search',methods=['post'])
def search():
    if session['lg'] == "lin":
        s=request.form['srch']
        q1="select * from mayor where mayor_name like '%"+s+"%'"
        res=db.select(q1)
        print(res)
        return  render_template("admin/viewmayor.html",data=res)
    else:
        return render_template("login.html")

#councillor mgt----------------------------------------------

@app.route('/admin_add_councillor')
def admin_add_councillor():
    if session['lg'] == "lin":
        return render_template("admin/addcouncillor.html")
    else:
        return render_template("login.html")

@app.route('/add_councillor',methods=['post'])
def add_councillor():
    if session['lg'] == "lin":
        name = request.form['textfield']
        gender = request.form['RadioGroup1']
        dob = request.form['textfield3']
        house_name = request.form['textfield2']
        place = request.form['textfield5']
        ph = request.form['textfield6']
        pin = request.form['textfield10']
        dis = request.form['textfield9']
        email = request.form['textfield4']
        ward=request.form['textfield8']
        pic = request.files['fileField']
        date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        pic.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\councillor\\" +date + ".jpg")
        path = "/static/councillor/" + date+ ".jpg"
        print(path)
        q3="select * from councillor where ward='"+str(ward)+"'"
        re3=db.selectOne(q3)

        if re3 is None:

            q2 = "insert into logintable(username,password,usertype)values('" + email + "','councillors','councillors')"
            res = db.insert(q2)
            print(res)
            q1 = "insert into councillor(name,gender,dob,house_name,place,pincode,phone,email,district,ward,login_id,image,joindate,enddate) values('"+name+"','"+gender+"','"+dob+"','"+house_name+"','"+place+"','"+pin+"','"+ph+"','"+email+"','"+dis+"','"+ward+"','"+str(res)+"','"+path+"',curdate(),date_add(curdate(),interval 1825 day))"
            res1 = db.insert(q1)
            return admin_add_councillor()

        #
        else:
            return "<script>alert('already added');window.location='/admin_add_councillor'</script>"
    else:
        return render_template("login.html")
@app.route('/admin_view_councillor')
def admin_view_councillor():
    if session['lg'] == "lin":
        q1="select logintable.*,councillor.* from councillor inner join logintable on logintable.login_id=councillor.login_id where logintable.usertype='councillors' "
        res=db.select(q1)
        return render_template("admin/viewcouncillor.html",data=res)
    else:
        return render_template("login.html")
@app.route('/coun_update/<i>')
def coun_update(i):
    if session['lg'] == "lin":
        q1 = "select * from councillor where councillor_id='"+i+"'"
        res = db.selectOne(q1)
        return render_template("admin/update councillor.html",data=res)
    else:
        return render_template("login.html")

@app.route('/coun_update_b',methods=['post'])
def coun_update_b():
    if session['lg'] == "lin":
        cid=request.form['cid']
        name = request.form['textfield']
        gender = request.form['RadioGroup1']
        dob = request.form['textfield3']
        house_name = request.form['textfield2']
        place = request.form['textfield5']
        ph = request.form['textfield6']
        pin = request.form['textfield10']
        dis = request.form['textfield9']
        # email = request.form['textfield4']
        ward = request.form['textfield8']
        pic = request.files['fileField']
        if request.files is not None:
            if pic.filename !="":
                data = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

                pic.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\councillor\\" + data + ".jpg")
                path = "/static/councillor/" + data + ".jpg"
                print(path)
                q1 = "update councillor set name='" + name + "',gender='" + gender + "',dob='" + dob + "',house_name='" + house_name + "',place='" + place + "',pincode='" + pin + "',phone='" + ph + "',district='" + dis + "',ward='" + ward + "',image='" + path + "' where councillor_id='"+cid+"'"
                res1 = db.update(q1)
                return admin_view_councillor()
            else:
                q2 = "update councillor set name='" + name + "',gender='" + gender + "',dob='" + dob + "',house_name='" + house_name + "',place='" + place + "',pincode='" + pin + "',phone='" + ph + "',district='" + dis + "',ward='" + ward + "' where councillor_id='" + cid + "'"
                res1 = db.update(q2)
                return admin_view_councillor()
        else:
            q2 = "update councillor set name='" + name + "',gender='" + gender + "',dob='" + dob + "',house_name='" + house_name + "',place='" + place + "',pincode='" + pin + "',phone='" + ph + "',district='" + dis + "',ward='" + ward + "' where councillor_id='" + cid + "'"
            res1 = db.update(q2)
            return admin_view_councillor()
    else:
        return render_template("login.html")


@app.route('/councillor_delete/<i>')
def councillor_delete(i):
    if session['lg'] == "lin":
        q4="delete from councillor where councillor_id='"+i+"'"
        res=db.delete(q4)
        return admin_view_councillor()
    else:
        return render_template("login.html")
@app.route('/searchcoun',methods=['post'])
def searchcoun():
    if session['lg'] == "lin":
        s = request.form['srch']
        q1="select * from councillor where name like '%"+s+"%'"
        res=db.select(q1)
        return render_template("admin/viewcouncillor.html",data=res)
    else:
        return render_template("login.html")
#dept mgt--------------------------------------------------------
@app.route('/admin_add_department')
def admin_add_department():
    if session['lg'] == "lin":
        return render_template("admin/departmentadd.html")
    else:
        return render_template("login.html")
@app.route('/add_dept',methods=['post'])
def add_dept():

    if session['lg'] == "lin":
        deptname=request.form['textfield']
        # a=request.form['button']
        print("-------------------------------")

        # print(a)
        # q2="insert into logintable(username,password,usertype) values('"+deptname+"','dept','dept')"
        # re=db.insert(q2)
        q1="insert into dept(name) values('"+deptname+"')"
        res=db.insert(q1)
        if int(res)>0:

            return admin_add_department()
        else:
                return "no"

    else:
        return render_template("login.html")
@app.route('/dept_update/<i>')
def dept_update(i):
    if session['lg'] == "lin":
        q1="select * from dept where dept_id='"+i+"'"
        res=db.selectOne(q1)
        return render_template("admin/departmentupdate.html",data=res)
    else:
        return render_template("login.html")
@app.route('/admin_view_department')
def admin_view_department():
    if session['lg'] == "lin":
        q1="select * from dept"
        res=db.select(q1)
        return render_template("admin/departmentview.html",data=res)
    else:
        return render_template("login.html")
@app.route('/update_b',methods=['post'])
def update_b():
    if session['lg'] == "lin":
        id=request.form['did']
        name=request.form["textfield"]
        q1="update dept set name='"+name+"' where dept_id='"+id+"'"
        res=db.update(q1)
        return admin_view_department()
    else:
        return render_template("login.html")
@app.route('/dept_delete/<i>')
def dept_delete(i):
    if session['lg'] == "lin":
        q4="delete from dept where dept_id='"+i+"'"
        res=db.delete(q4)
        return admin_view_department()
    else:
        return render_template("login.html")

@app.route('/searchdept',methods=['post'])
def searchdept():
    if session['lg'] == "lin":
        s = request.form['srch']
        q1="select * from dept where name like '%"+s+"%'"
        res=db.select(q1)
        return render_template("admin/departmentview.html", data=res)
    else:
        return render_template("login.html")
#clerk mgt-------------------------------------------------------------
@app.route('/admin_add_clerk')
def admin_add_clerk():
    q1 = "select * from dept"
    res = db.select(q1)
    return render_template("admin/addclerk.html",data=res)
@app.route('/add_clerk',methods=['post'])
def add_clerk():
    if session['lg'] == "lin":
        name = request.form['textfield']
        gender = request.form['RadioGroup1']
        dob = request.form['textfield3']
        house_name = request.form['textfield2']
        place = request.form['textfield5']
        ph = request.form['textfield6']
        pin = request.form['textfield10']
        dis = request.form['textfield9']
        email = request.form['textfield4']
        dept = request.form['select2']
        quali=request.form.getlist('q')

        str1=""
        for i in quali:
            str1=i+','+str1
            print(str1)
        pic = request.files['fileField']
        data = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

        pic.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\clerk\\" + data + ".jpg")
        path = "/static/clerk/" + data + ".jpg"
        print(path)

        q2 = "insert into logintable(username,password,usertype)values('" + email + "','clerk','clerks')"
        res = db.insert(q2)
        print(res)
        q1 = "insert into clerk(name,dept_id,dob,phone,email,gender,qualification,house_name,place,district,pin,image,login_id,joindate,enddate)values('"+name+"','"+dept+"','"+dob+"','"+ph+"','"+email+"','"+gender+"','"+str1+"','"+house_name+"','"+place+"','"+dis+"','"+pin+"','"+path+"','"+str(res)+"',curdate(),date_add(curdate(),interval 1825 day))"
        res1 = db.insert(q1)
        if int(res1) > 0:
            return admin_add_clerk()
    else:
        return  render_template("login.html")
@app.route('/admin_view_clerk')
def admin_view_clerk():
    if session['lg'] == "lin":
        q1="select clerk.*,dept.name as dname,dept.dept_id,logintable.* from clerk inner join dept on clerk.dept_id=dept.dept_id inner join logintable on logintable.login_id=clerk.login_id where logintable.usertype='clerks'"
        res=db.select(q1)
        return render_template("admin/viewclerk.html",data=res)
    else:
        return render_template("login.html")
@app.route('/clerk_update/<i>')
def clerk_update(i):
    if session['lg'] == "lin":

        q1 = "select clerk.*,dept.name as dname,dept.dept_id from clerk inner join dept on clerk.dept_id=dept.dept_id where clerk_id='"+i+"'"
        res=db.selectOne(q1)
        q2="select * from dept"
        r=db.select(q2)
        return render_template("admin/updateclerk.html",data=res,d=r)
    else:
        return render_template("login.html")

@app.route('/clerk_updateb',methods=['post'])
def clerk_updateb():
    if session['lg'] == "lin":
        cid=request.form['cid']
        name = request.form['textfield']
        gender = request.form['RadioGroup1']
        dob = request.form['textfield3']
        house_name = request.form['textfield2']
        place = request.form['textfield5']
        ph = request.form['textfield6']
        pin = request.form['textfield10']
        dis = request.form['textfield9']
        # email = request.form['textfield4']
        dept = request.form['select2']
        quali = request.form.getlist('q')
        str1 = ""
        for i in quali:
            str1 = i + ',' + str1
            print(str1)


        pic = request.files['fileField']

        if request.files is not None:
            if pic.filename !="":
                data = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                pic.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\clerk\\" + data + ".jpg")
                path = "/static/clerk/" + data + ".jpg"
                print(path)
                q1="update clerk set name='"+name+"',dept_id='"+dept+"',dob='"+dob+"',phone='"+ph+"',gender='"+gender+"',qualification='"+str1+"',house_name='"+house_name+"',place='"+place+"',district='"+dis+"',pin='"+pin+"',image='"+path+"' where clerk_id='"+cid+"'"
                res=db.update(q1)
                return admin_view_clerk()
            else:
                q2 = "update clerk set name='" + name + "',dept_id='" + dept + "',dob='" + dob + "',phone='" + ph + "',gender='" + gender + "',qualification='" + str1 + "',house_name='" + house_name + "',place='" + place + "',district='" + dis + "',pin='" + pin + "' where clerk_id='" + cid + "'"
                res = db.update(q2)
                return admin_view_clerk()
        else:
            q2 = "update clerk set name='" + name + "',dept_id='" + dept + "',dob='" + dob + "',phone='" + ph + "',gender='" + gender + "',qualification='" + str1 + "',house_name='" + house_name + "',place='" + place + "',district='" + dis + "',pin='" + pin + "' where clerk_id='" + cid + "'"
            res = db.update(q2)
            return admin_view_clerk()
    else:
        return render_template("login.html")
@app.route('/clerk_delete/<i>')
def clerk_delete(i):
    if session['lg'] == "lin":
        q4="delete from clerk where clerk_id='"+i+"'"
        res=db.delete(q4)
        return admin_view_clerk()
    else:
        return render_template("login.html")

@app.route('/searchclrk',methods=['post'])
def searchclrk():
    if session['lg'] == "lin":
        s = request.form['srch']
        q1="select * from clerk where name like '%"+s+"%'"
        res=db.select(q1)
        return render_template("admin/viewclerk.html", data=res)
    else:
        return render_template("login.html")

#coorperation mgt--------------------------------------------------------------------------


@app.route('/admin_add_coorperation')
def admin_add_coorperation():
    if session['lg'] == "lin":
        return render_template("admin/coorperationprofile.html")
    else:
        return render_template("login.html")
@app.route('/addcoorperation',methods=['post'])
def addcoorperation():
    if session['lg'] == "lin":
        name = request.form['textfield']
        place = request.form['textfield4']
        ph = request.form['textfield2']
        pin = request.form['textfield5']
        email = request.form['textfield3']
        pic = request.files['fileField']
        data = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        pic.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\coorperation\\" + data + ".jpg")
        path = "/static/coorperation/" + data + ".jpg"
        print(path)
        q2 = "insert into logintable(username,password,usertype)values('" + email + "','coorperation','coorperation')"
        res = db.insert(q2)
        print(res)
        q3="insert into corporationprofile(name,email,phone,place,pin,image,login_id)values('"+name+"','"+email+"','"+ph+"','"+place+"','"+pin+"','"+path+"','"+str(res)+"')"
        res1 = db.insert(q3)
        if int(res1) > 0:
            return  admin_add_coorperation()
    else:
        return render_template("login.html")
@app.route('/admin_view_coorperation')
def admin_view_coorperation():
    if session['lg'] == "lin":
        q1="select * from corporationprofile"
        res=db.select(q1)
        return render_template("admin/coorperationview.html",data=res)
    else:
        return render_template("login.html")
@app.route('/coorperation_update/<i>')
def coorperation_update(i):
    if session['lg'] == "lin":
        q1="select * from corporationprofile where profile_id='"+i+"' "
        res=db.selectOne(q1)
        return render_template("admin/coorperationupdate.html",data=res)
    else:
        return render_template("login.html")
@app.route('/coorperation_update_b',methods=['post'])
def coorperation_update_b():
    if session['lg'] == "lin":
        coid=request.form['coid']
        name = request.form['textfield']
        place = request.form['textfield4']
        ph = request.form['textfield2']
        pin = request.form['textfield5']
        # email = request.form['textfield3']
        pic = request.files['fileField']
        data = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        if request.files is not None:

            if pic.filename !="":
                pic.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\coorperation\\" + data + ".jpg")
                path = "/static/coorperation/" + data + ".jpg"
                print(path)
                q2="update corporationprofile set name='"+name+"',phone='"+ph+"',place='"+place+"',pin='"+pin+"',image='"+path+"' where profile_id='"+coid+"'"
                res=db.update(q2)
                return admin_view_coorperation()
            else:
                q3 = "update corporationprofile set name='" + name + "',phone='" + ph + "',place='" + place + "',pin='" + pin + "' where profile_id='" + coid + "'"
                res = db.update(q3)
                return admin_view_coorperation()
        else:
            q3 = "update corporationprofile set name='" + name + "',phone='" + ph + "',place='" + place + "',pin='" + pin + "' where profile_id='" + coid + "'"
            res = db.update(q3)
            return admin_view_coorperation()
    else:
        return render_template("login.html")


@app.route('/coorperation_delete/<i>')
def coorperation_delete(i):
    if session['lg'] == "lin":
        q1 = "delete from corporationprofile where profile_id='"+i+"'"
        res=db.delete(q1)
        return admin_view_coorperation()
    else:
        return render_template("login.html")


# depthead mgt-----------------------------------------------------------------------------------------
@app.route('/admin_add_departmenthead')
def admin_add_departmenthead():
    if session['lg'] == "lin":
        q1="select * from dept"
        res=db.select(q1)
        q2="select * from  clerk"
        r=db.select(q2)
        return render_template("admin/department_head_add.html",data=res,d=r)
    else:
        return render_template("login.html")
@app.route('/add_departmenthead',methods=['post'])
def add_departmenthead():
    if session['lg'] == "lin":
        deptid=request.form['select2']
        cid=request.form['select']
        # hid=request.form['log']
        # print(hid)
        q4="select clerk.*,logintable.login_id as i from logintable inner join clerk on clerk.login_id=logintable.login_id where clerk.clerk_id='"+str(cid)+"'"
        r=db.selectOne(q4)
        r1=r['i']
        print(r1)
        q3="update logintable set usertype='dept' where login_id='"+str(r1)+"'"
        r=db.update(q3)
        q2="insert into depthead(clerk_id,dept_id)values('"+cid+"','"+deptid+"')"
        res=db.insert(q2)
        return  admin_add_departmenthead()
    else:
        return render_template("login.html")
@app.route('/admin_view_departmenthead')
def admin_view_departmenthead():
    if session['lg'] == "lin":
        q2="select depthead.*,clerk.*,dept.dept_id,dept.name as d from depthead inner join clerk on depthead.clerk_id=clerk.clerk_id inner join dept on dept.dept_id=depthead.dept_id"
        res=db.select(q2)
        return render_template("admin/department_head_view.html",d=res)
    else:
        return render_template("login.html")

@app.route('/dept_head_update/<i>')
def dept_head_update(i):
    if session['lg'] == "lin":
        q1="select depthead.*,clerk.*,dept.dept_id,dept.name as d from depthead inner join clerk on depthead.clerk_id=clerk.clerk_id inner join dept on dept.dept_id=depthead.dept_id where head_id='"+i+"'"
        res=db.selectOne(q1)

        q1 = "select * from dept"
        re = db.select(q1)
        q2 = "select * from  clerk"
        r = db.select(q2)
        return render_template("admin/department_head_update.html",data=res,d1=re,d2=r)
    else:
        return render_template("login.html")
@app.route('/dept_head_updateb',methods=['post'])
def dept_head_updateb():
    if session['lg'] == "lin":
        hid=request.form['hid']
        deptid = request.form['select2']
        cid = request.form['select']
        q2 = "update depthead set clerk_id='" + cid + "',dept_id='" + deptid + "' where head_id='"+hid+"'"
        res=db.update(q2)
        return admin_view_departmenthead()
    else:
        return render_template("login.html")
@app.route('/dept_head_delete/<i>')
def dept_head_delete(i):
    if session['lg'] == "lin":
        q1=" delete from depthead where head_id='"+i+"'"
        res=db.delete(q1)
        return  admin_view_departmenthead()
    else:
        return render_template("login.html")
@app.route('/searchhead',methods=['post'])
def searchhead():
    if session['lg'] == "lin":
        s = request.form['srch']
        q2 = "select depthead.*,clerk.*,dept.dept_id,dept.name as d from depthead inner join clerk on depthead.clerk_id=clerk.clerk_id inner join dept on dept.dept_id=depthead.dept_id where dept.name like '%"+s+"%'  or clerk.name like '%"+s+"%'"
        res = db.select(q2)
        return render_template("admin/department_head_view.html", d=res)
    else:
        return render_template("login.html")

# adminend--------------------------------------------------------------------------------------------------------------


# mayor-----------------------------------------------------------------------------------------------------------------
@app.route('/mayor_home')
def mayor_home():
    if session['lg']=="lin":
        return render_template("mayor/mayor_home.html")
    else:
        return  render_template("login.html")

# ------------------------------------------------------------------
@app.route('/mayor_add_meeting')
def mayor_add_meeting():
    if session['lg']=="lin":
        return render_template("mayor/add meeting.html")
    else:
        return  render_template("login.html")

# ------------------------------------------------------------------
@app.route('/mayor_add_meeting_post',methods=['post'])
def mayor_add_meeting_post():
    if session['lg']=="lin":

        date=request.form['textfield2']
        time=request.form['textfield3']
        venue=request.form['textfield4']
        topic=request.form['textfield5']
        a = session['login_id']
        q1="insert into meeting(mayorid,date,time,venue,topic) values('"+str(a)+"','"+date+"','"+time+"','"+venue+"','"+topic+"')"
        res=db.insert(q1)
        return render_template("mayor/add meeting.html")
    else:
        return  render_template("login.html")

@app.route('/mayor_view_meeting')
def mayor_view_meeting():
    if session['lg']=="lin":
        q1="select * from meeting ORDER  by date DESC "
        res=db.select(q1)
        return render_template("mayor/view meeting.html",data=res)
    else:
        return  render_template("login.html")
@app.route('/mayor_edit_meeting/<i>')
def mayor_edit_meeting(i):
    if session['lg']=="lin":
        q1 = "select * from meeting where meetingid='"+i+"'"
        res = db.selectOne(q1)
        print(res['time'])
        return render_template("mayor/editmeeting.html",data=res)
    else:
        return  render_template("login.html")
@app.route('/mayor_edit_meeting_post',methods=['post'])
def mayor_edit_meeting_post():
    if session['lg']=="lin":
        did=request.form['textfield']
        date = request.form['textfield2']
        time = request.form['textfield3']
        venue = request.form['textfield4']
        topic = request.form['textfield5']
        a = session['login_id']
        q1="update  meeting set date='"+date+"',time='"+time+"',venue='"+venue+"',topic='"+topic+"' where meetingid='"+did+"' and mayorid='"+str(a)+"'"
        res=db.update(q1)
        return mayor_view_meeting()
    else:
        return  render_template("login.html")

@app.route('/dltmeeting/<i>')
def dltmeeting(i):
    if session['lg'] == "lin":
        q1="delete from meeting where meetingid='"+i+"'"
        res=db.delete(q1)
        return mayor_view_meeting()
    else:
        return  render_template("login.html")

# -------------------------------------------------------------
@app.route('/mayor_add_application_category')
def mayor_add_application_category():
    if session['lg'] == "lin":
        dept="select * from dept"
        res=db.select(dept)
        return render_template("mayor/application category.html",d=res)
    else:
        return  render_template("login.html")
@app.route('/mayor_add_application_category1',methods=['post'])
def mayor_add_application_category1():
    if session['lg'] == "lin":
        cat=request.form['textfield']
        dept=request.form['textfield2']
        des=request.form['textarea']
        a = session['login_id']
        q2="insert into applcncatagory(category,dept_id,description,mid) values('"+cat+"','"+dept+"','"+des+"','"+str(a)+"')"
        res=db.insert(q2)
        return mayor_add_application_category()
    else:
        return  render_template("login.html")


@app.route('/mayor_edit_application_category/<i>')
def mayor_edit_application_category(i):
    if session['lg'] == "lin":

        dept="select * from dept"
        res1=db.select(dept)
        q2="select applcncatagory.*,dept.* from applcncatagory inner join dept on applcncatagory.dept_id=dept.dept_id where cat_id='"+i+"'"
        res=db.selectOne(q2)
        return render_template("mayor/edit app  category.html",d=res,data=res1)
    else:
        return  render_template("login.html")
@app.route('/mayor_edit_application_categoryb',methods=['post'])
def mayor_edit_application_categoryb():
    if session['lg'] == "lin":
        cat = request.form['textfield']
        dept = request.form['textfield2']
        des = request.form['textarea']
        cid= request.form['cid']
        q2="update applcncatagory set category='"+cat+"',dept_id='"+dept+"',description='"+des+"' where cat_id='"+cid+"'"
        res=db.update(q2)
        return mayor_view_application_category()
    else:
        return  render_template("login.html")

@app.route('/mayor_view_application_category')
def mayor_view_application_category():
    if session['lg'] == "lin":
        q2="select applcncatagory.*,dept.* from applcncatagory inner join dept on applcncatagory.dept_id=dept.dept_id"
        res=db.select(q2)
        return render_template("mayor/view app category.html",data=res)
    else:
        return  render_template("login.html")
@app.route('/dltapp/<i>')
def dltapp(i):
    if session['lg'] == "lin":
        q2="delete from applcncatagory where cat_id='"+i+"'"
        res=db.delete(q2)
        return mayor_view_application_category()
    else:
        return  render_template("login.html")


# -----------------------------------------------------------------
@app.route('/mayor_add_certificate_category')
def mayor_add_certificate_category():
    if session['lg'] == "lin":
        dept = "select * from dept"
        res = db.select(dept)
        return render_template("mayor/certificat category.html",d=res)
    else:
        return  render_template("login.html")
@app.route('/mayor_add_certificate_category1',methods=['post'])
def mayor_add_certificate_category1():
    if session['lg'] == "lin":
        cat=request.form['textfield']
        dept=request.form['textfield2']
        des=request.form['textarea']
        a = session['login_id']
        q2="insert into certficatecategory(category,dept_id,description,mid) values('"+cat+"','"+dept+"','"+des+"','"+str(a)+"')"
        res=db.insert(q2)
        return mayor_add_certificate_category()
    else:
        return render_template("login.html")


@app.route('/mayor_edit_certificate_category/<i>')
def mayor_edit_certificate_category(i):
    if session['lg'] == "lin":

        dept="select * from dept"
        res1=db.select(dept)
        q2="select certficatecategory.*,dept.* from certficatecategory inner join dept on certficatecategory.dept_id=dept.dept_id where category_id='"+i+"'"
        res=db.selectOne(q2)
        return render_template("mayor/edit cert category.html",d=res,data=res1)
    else:
        return render_template("login.html")


@app.route('/mayor_edit_cert_categoryb',methods=['post'])
def mayor_edit_cert_categoryb():
    if session['lg'] == "lin":
        cat = request.form['textfield']
        dept = request.form['textfield2']
        des = request.form['textarea']
        cid= request.form['cid']
        q2="update certficatecategory set category='"+cat+"',dept_id='"+dept+"',description='"+des+"' where category_id='"+cid+"'"
        res=db.update(q2)
        return mayor_view_certificate_category()
    else:
        return render_template("login.html")


@app.route('/mayor_view_certificate_category')
def mayor_view_certificate_category():
    if session['lg'] == "lin":
        q2 = "select certficatecategory.*,dept.* from certficatecategory inner join dept on certficatecategory.dept_id=dept.dept_id"
        res = db.select(q2)
        return render_template("mayor/view cert category.html",data=res)
    else:
        return render_template("login.html")

@app.route('/dltcerti/<i>')
def dltcerti(i):
    if session['lg'] == "lin":

        q2="delete from certficatecategory where category_id='"+i+"'"
        res=db.delete(q2)
        return mayor_view_certificate_category()
    else:
        return render_template("login.html")

# ----------------------------------------------------------------------
@app.route('/mayor_view_councillor_rating')
def mayor_view_councillor_rating():
    if session['lg'] == "lin":
        q2="select councillor.name,councillor.image,councillor.councillor_id,councillorrating.*,user.name as u,user.image  as photo,user.user_id,logintable.* from councillorrating inner join councillor on councillorrating.councillor_id=councillor.login_id inner join user on councillorrating.user_id=user.login_id inner join logintable on logintable.login_id=councillor.login_id where logintable.usertype='councillors'"
        res=db.select(q2)
        return render_template("mayor/coun rating.html",i=res)
    else:
        return render_template("login.html")

@app.route('/mayor_view_department_rating')
def mayor_view_department_rating():
    if session['lg'] == "lin":
        q2="select departmentrating.*,user.name as uname,user.image as img,user.user_id,dept.dept_id,dept.name as dname from departmentrating inner join dept on dept.dept_id=departmentrating.dept_id inner join user on user.user_id=departmentrating.user_id"
        res=db.select(q2)
        return render_template("mayor/dept rating.html",data=res)
    else:
        return render_template("login.html")



# --------------------------------------------------------------------------
@app.route('/councillor_chat')
def councillor_chat():
    if session['lg'] == "lin":

        return render_template("mayor/couns_mayor_chat.html")
    else:
        return render_template("login.html")

@app.route('/mayor_mayor_councillor_chat',methods=['post'])
def mayor_mayor_councillor_chat():
    if session['lg'] == "lin":
        a=session['login_id']
        q1 = "select councillor.*,logintable.login_id,logintable.usertype from councillor inner join logintable on logintable.login_id=councillor.login_id where logintable.usertype='councillors'"
        res = db.select(q1)
        v={}
        if len(res)>0:
            v["status"]="ok"
            v['data']=res
        else:
            v["status"]="error"

        rw=demjson.encode(v)
        print(rw)
        return rw
    else:
        return render_template("login.html")
@app.route('/chatsnd',methods=['post'])
def chatsnd():
    if session['lg'] == "lin":
        c = session['login_id']
        b=request.form['n']
        print(b)
        m=request.form['m']

        q2="insert into councillormayorchat(from_id,to_id,messege,date) values('"+str(c)+"','"+str(b)+"','"+m+"',curdate())"
        res=db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r
    else:
        return render_template("login.html")
@app.route('/chatrply',methods=['post'])
def chatrply():
    if session['lg'] == "lin":
        print("...........................")
        c = session['login_id']
        b=request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from councillormayorchat ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id']=c
        else:
            v["status"] = "error"
        rw = demjson.encode(v)
        return rw
    else:
        return render_template("login.html")


# ---------------------------------------------------------------------------
@app.route('/mayor_add_fundallocatn_to_councillor')
def mayor_add_fundallocatn_to_councillo():
    if session['lg'] == "lin":
        q2="select councillor.councillor_id,councillor.name from councillor"
        res=db.select(q2)
        return render_template("mayor/fund_alloc_to_couns.html",d=res)
    else:
        return render_template("login.html")
@app.route('/mayor_add_fundallocatn_to_councillorb',methods=['post'])
def mayor_add_fundallocatn_to_councillorb():
    if session['lg'] == "lin":
        c=request.form['select']
        fund=request.form['textfield']
        a = session['login_id']
        q2="insert into fundalloctocouncillor(fund,councillor_id,mayor_id,date) values('"+c+"','"+str(a)+"','"+fund+"',curdate())"
        res=db.insert(q2)
        return mayor_add_fundallocatn_to_councillo()
    else:
        return render_template("login.html")


@app.route('/mayor_view_fundallocatn_to_councillor')
def mayor_view_fundallocatn_to_councillor():
    if session['lg'] == "lin":
        a = session['login_id']
        q2="select councillor.name as cname,councillor.gender,councillor.dob,councillor.house_name,councillor.place,councillor.pincode,councillor.phone,councillor.email,councillor.district,councillor.ward,councillor.image,fundalloctocouncillor.* from fundalloctocouncillor inner join councillor on fundalloctocouncillor.councillor_id=councillor.councillor_id where fundalloctocouncillor.mayor_id='"+str(a)+"'"
        res=db.select(q2)
        print(q2)

        return render_template("mayor/fund_alloc_to_cous_report.html",data=res)
    else:
        return render_template("login.html")
@app.route('/fundcounmore/<i>/<m>')
def fundcounmore(i,m):
    if session['lg'] == "lin":
        mid=str(m)
        cid=str(i)
        q2="select councillor.name as cname,councillor.gender,councillor.dob,councillor.house_name,councillor.place,councillor.pincode,councillor.phone,councillor.email,councillor.district,councillor.ward,councillor.image,fundalloctocouncillor.* from fundalloctocouncillor inner join councillor on fundalloctocouncillor.councillor_id=councillor.councillor_id where fundalloctocouncillor.mayor_id='"+mid+"' and fundalloctocouncillor.councillor_id='"+cid+"'"
        res=db.selectOne(q2)
        return render_template("mayor/fundcouncmore.html",i=res)

    else:
        return render_template("login.html")
# ----------------------------------------------------------------------------
@app.route('/mayor_add_service')
def mayor_add_service():
    if session['lg'] == "lin":
        return render_template("mayor/service manegmenmt.html")
    else:
        return render_template("login.html")
@app.route('/mayor_add_serviceb',methods=['post'])
def mayor_add_serviceb():
    if session['lg'] == "lin":
        a = session['login_id']
        name=request.form['textfield']
        des=request.form['textarea']
        q1="insert service(name,description,m_id) values('"+name+"','"+des+"','"+str(a)+"')"
        res=db.insert(q1)
        return  mayor_add_service()
    else:
        return render_template("login.html")
@app.route('/mayor_edit_service/<i>')
def mayor_edit_service(i):
    if session['lg'] == "lin":
        q1 = "select * from service where service_id='"+i+"'"
        res = db.selectOne(q1)
        return render_template("mayor/edit service manegmenmt.html",i=res)
    else:
        return render_template("login.html")
@app.route('/mayor_edit_services',methods=['post'])
def mayor_edit_services():
    if session['lg'] == "lin":
        a = request.form['sid']
        name=request.form['textfield']
        des=request.form['textarea']
        q1="update service set  name='"+name+"',description='"+des+"' where service_id='"+a+"'"
        e=db.update(q1)
        return mayor_view_service()
    else:
        return render_template("login.html")

@app.route('/mayor_view_service')
def mayor_view_service():
    if session['lg'] == "lin":
        q1="select * from service"
        res=db.select(q1)
        return render_template("mayor/view service.html",data=res)
    else:
        return render_template("login.html")
@app.route('/dltservice/<i>')
def dltservice(i):
    if session['lg'] == "lin":
        q1 = "delete from service where service_id='"+i+"'"
        res = db.delete(q1)
        return mayor_view_service()
    else:
        return render_template("login.html")

# -----------------------------------------------------------------------------
@app.route('/mayor_add_notification')
def mayor_add_notification():
    if session['lg'] == "lin":
        return render_template("mayor/notification.html")
    else:
        return render_template("login.html")
@app.route('/addnotifi',methods=['post'])
def addnotifi():
    if session['lg'] == "lin":
        name = request.form['textfield']
        des = request.form['textarea']
        a = session['login_id']
        q2="insert into notification(subject,description,date,mayor_id) values('"+name+"','"+des+"',curdate(),'"+str(a)+"')"
        res=db.insert(q2)
        return mayor_add_notification()
    else:
        return render_template("login.html")
@app.route('/mayor_view_notification')
def mayor_view_notification():
    if session['lg'] == "lin":
        a = session['login_id']
        q2="select * from notification where mayor_id='"+str(a)+"' "
        res=db.select(q2)
        return render_template("mayor/view_notification.html",data=res)
    else:
        return render_template("login.html")

@app.route('/mayor_edit_notification/<i>/<m>')
def mayor_edit_notification(i,m):
    if session['lg'] == "lin":
        q2 = "select * from notification where mayor_id='" + str(m) +"' and notification_id='"+str(i)+"'  "
        res=db.selectOne(q2)
        return render_template("mayor/enotification.html",i=res)
    else:
        return render_template("login.html")
@app.route('/mayor_view_notificationb',methods=['post'])
def mayor_view_notificationb():
    if session['lg'] == "lin":
        name = request.form['textfield']
        des = request.form['textarea']
        id=request.form['sid']
        q2="update notification set subject='"+name+"',description='"+des+"',date=curdate() where notification_id='"+str(id)+"'"
        res=db.update(q2)
        return mayor_view_notification()
    else:
        return render_template("login.html")
@app.route('/mdltnotfi/<i>')
def mdltnotfi(i):
    if session['lg'] == "lin":
        q2="delete from notification where notification_id='"+str(i)+"'"
        res=db.delete(q2)
        return mayor_view_notification()
    else:
        return render_template("login.html")

# ------------------------------------------------------------------------------


@app.route('/mayor_view_fundallocatn_to_coordinator')
def mayor_view_fundallocatn_to_coordinator():
    if session['lg'] == "lin":
        q2="select coordinator.*,fundalloctocoodinator.*,councillor.councillor_id,councillor.name as cname,councillor.image as i from councillor inner join fundalloctocoodinator on fundalloctocoodinator.councillor_id=councillor.councillor_id inner join coordinator on fundalloctocoodinator.cood_id=coordinator.coordinator_id"
        res=db.select(q2)
        return render_template("mayor/fund_alloc_to_cood_report.html",d=res)
    else:
        return render_template("login.html")
@app.route('/morefc/<i>/<m>')
def morefc(i,m):
    if session['lg'] == "lin":
        q2="select coordinator.*,fundalloctocoodinator.*,councillor.councillor_id,councillor.name as cname,councillor.image as i,councillor.house_name,councillor.place,councillor.pincode,councillor.phone as p,councillor.ward from councillor inner join fundalloctocoodinator on fundalloctocoodinator.councillor_id=councillor.councillor_id inner join coordinator on fundalloctocoodinator.cood_id=coordinator.coordinator_id where fundalloctocoodinator.cood_id='"+str(i)+"' and  fundalloctocoodinator.councillor_id='"+str(m)+"'"
        res=db.selectOne(q2)
        return render_template("mayor/fundmorecoor.html",i=res)
    else:
        return render_template("login.html")

# ----------------------------------------------------------------------------------

@app.route('/mayor_view_public_usage_report')
def mayor_view_public_usage_report():
    if session['lg'] == "lin":
        q2="select publicneedreport.*,coordinator.*,publicneedfundalloc.* from publicneedfundalloc inner join publicneedreport on publicneedfundalloc.report_id=publicneedreport.report_id inner join coordinator on coordinator.login_id=publicneedreport.cood_id ORDER BY publicneedreport.issue_date DESC "
        res=db.select(q2)

        return render_template("mayor/public useage_report.html",d=res)
    else:
        return render_template("login.html")
# ------------------------------------------------------------------------------------

@app.route('/mayor_view_policies')
def mayor_view_policies():
    if session['lg'] == "lin":
        q2="select policy.name as pname,policy.policy_id,policy.councillor_id,policy.description,policy.date,policy.status,councillor.* from policy inner join councillor on policy.councillor_id=councillor.login_id where status='pending'"
        res=db.select(q2)
        return render_template("mayor/view polices.html",d=res)
    else:
        return render_template("login.html")
@app.route('/more/<i>')
def more(i):
    if session['lg'] == "lin":
        q2="select policy.name as pname,policy.policy_id,policy.councillor_id,policy.description,policy.date,policy.status,councillor.* from policy inner join councillor on policy.councillor_id=councillor.login_id where status='pending' and policy.policy_id='"+str(i)+"'"
        res=db.selectOne(q2)
        return render_template("mayor/morepolicy.html",i=res)
    else:
        return render_template("login.html")
@app.route('/mb',methods=['post'])
def mb():
    if session['lg'] == "lin":
        idp=request.form['b']
        acc=request.form['a']
        if acc=='ACCEPT':
            q2="update policy set status='accept' where policy_id='"+str(idp)+"'"
            res=db.update(q2)
            return mayor_view_policies()
        if acc=="REJECT":
            q2 = "update policy set status='reject' where policy_id='" + str(idp) + "'"
            res = db.update(q2)
            return mayor_view_policies()
    else:
        return render_template("login.html")


# --------------------------------------------------------------------------------------
@app.route('/mayor_add_project')
def mayor_add_project():
    if session['lg'] == "lin":
        return render_template("mayor/project_manegment.html")
    else:
        return render_template("login.html")
@app.route('/mayor_add_projectb',methods=['post'])
def mayor_add_projectb():
    if session['lg'] == "lin":
        name=request.form['textfield']
        des=request.form['textarea']
        a = session['login_id']
        ed = request.form['textfield3']
        amnt = request.form['textfield4']
        q2="insert into project(name,details,status,date,uid,amount,enddate) values('"+name+"','"+des+"','pending',curdate(),'"+str(a)+"','"+amnt+"','"+ed+"')"
        res=db.insert(q2)
        return mayor_add_project()
    else:
        return render_template("login.html")

@app.route('/mayor_view_project')
def mayor_view_project():
    if session['lg'] == "lin":
        a = session['login_id']
        q2="select * from project where uid='"+str(a)+"' ORDER  by date DESC "
        res=db.select(q2)
        return render_template("mayor/viewproject.html",data=res)
    else:
        return render_template("login.html")
@app.route('/mayor_edit_project/<i>')
def mayor_edit_project(i):
    if session['lg'] == "lin":
        q2 = "select * from project where project_id='"+i+"'"
        res=db.selectOne(q2)
        return render_template("mayor/edit project.html",i=res)
    else:
        return render_template("login.html")
@app.route('/editpro',methods=['post'])
def editpro():
    if session['lg'] == "lin":
        pid=request.form['pid']
        name = request.form['textfield']
        des = request.form['textarea']
        ed = request.form['textfield3']
        amnt = request.form['textfield4']
        statuss = request.form['s']
        q2="update project set name='"+name+"',details='"+des+"',date=curdate(),amount='"+amnt+"',enddate='"+ed+"',status='"+statuss+"' where project_id='"+pid+"'"
        print(q2)
        res=db.update(q2)
        print(res)
        return mayor_view_project()
    else:
        return render_template("login.html")


@app.route('/dltprjct/<i>')
def dltprjct(i):
    if session['lg'] == "lin":
        q2 = "delete from project where project_id='"+i+"' and status='pending'"
        res=db.delete(q2)
        return mayor_view_project()
    else:
        return render_template("login.html")

# -----------------------------------------------------------------------------------------

@app.route('/mayor_view_suggestion')
def mayor_view_suggestion():
    if session['lg'] == "lin":
        q2="select suggestion.*,user.name,user.image,user.login_id from user inner join suggestion on suggestion.user_id=user.login_id order by date DESC "
        res=db.select(q2)
        return render_template("mayor/view_suggetion.html",data=res)
    else:
        return render_template("login.html")

# mayorend--------------------------------------------------------------------------------------------------------------
# department------------------------------------------------------------------------------------------------------------
@app.route('/dept_add_work')
def dept_add_work():
    if session['lg'] == "lin":
        a=session['login_id']
        print(a)
        q2="select clerk.*,dept.name as s,dept.dept_id,depthead.head_id,depthead.clerk_id as i,depthead.dept_id from clerk inner join dept on clerk.dept_id=dept.dept_id inner join depthead on depthead.dept_id=dept.dept_id where  clerk.login_id!='"+str(a)+"'"
        res=db.select(q2)
        return render_template("dept/work manegment.html",d=res)
    else:
        return render_template("login.html")
@app.route('/depaddworkb',methods=['post'])
def depaddworkb():
    if session['lg'] == "lin":
        c=request.form['select']
        w=request.form['textfield']
        a = session['login_id']
        print(c,a)
        q2="insert into work(dept_head_id,clerk_id,work_details,date,status) values('"+str(a)+"','"+str(c)+"','"+w+"',curdate(),'pending')"
        res=db.insert(q2)
        q3="insert into work_report(work_id,work_status,description,date,cid) values('"+str(res)+"','pending','pending','pending','"+str(c)+"')"
        r=db.insert(q3)
        return dept_add_work()
    else:
        return render_template("login.html")


@app.route('/dept_work_view')
def dept_work_view():
    if session['lg'] == "lin":
        a = session['login_id']
        q2="select clerk.*,dept.name as s,dept.dept_id,depthead.head_id,depthead.clerk_id as i,depthead.dept_id,work.* from clerk inner join dept on clerk.dept_id=dept.dept_id inner join depthead on depthead.dept_id=dept.dept_id inner join work on work.dept_head_id=clerk.login_id where  clerk.login_id='"+str(a)+"' and work.status='pending'"
        res=db.select(q2)
        return render_template("dept/view work report.html",d=res)
    else:
        return render_template("login.html")


@app.route('/clerk_view')
def clerk_view():
    if session['lg'] == "lin":
        a = session['login_id']
        q1 = "select clerk.*,dept.name as dname,dept.dept_id from clerk inner join dept on clerk.dept_id=dept.dept_id where  clerk.login_id!='"+str(a)+"'"
        res = db.select(q1)
        return render_template("dept/view clerk.html", data=res)
    else:
        return render_template("login.html")
@app.route('/searchclrks',methods=['post'])
def searchclrks():
    if session['lg'] == "lin":
        s = request.form['srch']
        q1="select * from clerk where name like '%"+s+"%'"
        res=db.select(q1)
        return render_template("dept/view clerk.html", data=res)
    else:
        return render_template("login.html")


@app.route('/dept_appl_reqst')
def dept_appl_reqst():
    if session['lg'] == "lin":

        return render_template("dept/view appl req.html")
    else:
        return render_template("login.html")

@app.route('/dept_cert_reqstd')
def dept_cert_reqstd():
    if session['lg'] == "lin":
         return render_template("dept/view cert  req.html")
    else:
        return render_template("login.html")

@app.route('/rating')
def rating():
    if session['lg'] == "lin":
        q2="select departmentrating.*,user.name as uname,user.image as img,user.user_id,dept.dept_id,dept.name as dname from departmentrating inner join dept on dept.dept_id=departmentrating.dept_id inner join user on user.user_id=departmentrating.user_id"
        res=db.select(q2)
        return render_template("dept/dept rating.html",data=res)
    else:
        return render_template("login.html")
@app.route('/n')
def n():
    if session['lg'] == "lin":
        a = session['login_id']
        q2="select notification.*,logintable.* from logintable inner join notification on logintable.login_id=notification.mayor_id where logintable.usertype='mayor'"
        res=db.select(q2)
        return render_template("dept/deptnotification.html",data=res)
    else:
        return render_template("login.html")

@app.route('/wstatus')
def wstatus():
    if session['lg'] == "lin":
        a = session['login_id']
        q2="select work.*,work_report.*,clerk.* from work inner join work_report on work_report.work_id=work.work_id inner join clerk on work.clerk_id=clerk.login_id  where work.dept_head_id='"+str(a)+"' and work_report.work_status='Complete'"
        res=db.select(q2)
        return render_template("dept/wstatus.html",d=res)
    else:
        return render_template("login.html")
# detend----------------------------------------------------------------------------------------------------------------
# clerk-----------------------------------------------------------------------------------------------------------------

@app.route('/clerk_view_notification')
def clerk_view_notification():
    if session['lg'] == "lin":
        a = session['login_id']
        q2 = "select notification.*,logintable.* from logintable inner join notification on logintable.login_id=notification.mayor_id where logintable.usertype='mayor'"
        res = db.select(q2)
        return render_template("clerk/clerknotification.html",data=res)
    else:
        return render_template("login.html")

@app.route('/clerk_view_department_rating')
def clerk_view_department_rating():
    if session['lg'] == "lin":

        q2 = "select departmentrating.*,user.name as uname,user.image as img,user.user_id,dept.dept_id,dept.name as dname from departmentrating inner join dept on dept.dept_id=departmentrating.dept_id inner join user on user.user_id=departmentrating.user_id"
        res = db.select(q2)

        return render_template("clerk/dept rating.html",data=res)
    else:
        return render_template("login.html")



@app.route('/view_appli_request')
def view_appli_request():
    if session['lg'] == "lin":
        return render_template("clerk/view application request.html")
    else:
        return render_template("login.html")


@app.route('/view_certi_request')
def view_certi_request():
    if session['lg'] == "lin":

        return render_template("clerk/view certificate request.html")
    else:
        return render_template("login.html")

@app.route('/view_alloc_work')
def view_alloc_work():
    if session['lg'] == "lin":
        a = session['login_id']
        q2="select work.*,clerk.*,depthead.* from clerk inner join work on work.clerk_id=clerk.login_id inner join depthead on depthead.dept_id=clerk.dept_id where clerk.login_id='"+str(a)+"' and work.status!='Complete'"
        res=db.select(q2)
        return render_template("clerk/view alloc work.html",d=res)
    else:
        return render_template("login.html")


@app.route('/work_report/<i>')
def work_report(i):
    if session['lg'] == "lin":
        a=session['login_id']
        print(i)
        return render_template("clerk/work report.html",data=i)
    else:
        return render_template("login.html")

@app.route('/work_reportb', methods=['post'])
def work_reportb():
    if session['lg'] == "lin":
            a=session['login_id']
            n=request.form['n']
            status = request.form['select']
            des = request.files['textarea']
            data = datetime.datetime.now().strftime("%y%m%d-%H%S%M")
            des.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\clerkworkreport\\" + data + ".pdf")
            path = "/static/clerkworrkreport/" + data + ".pdf"

            if status=='Complete':
                print("complete")

                q2 = "update  work_report set work_status='" + status + "',description='" + path + "',date=now() where work_id='" + str(n) + "' and cid='"+str(a)+"'"
                res = db.update(q2)
                q3="update work set status='complete' where clerk_id='"+str(a)+"' and work_id='"+str(n)+"'"
                e=db.update(q3)
                print("mmmmmmmmmmm",q2,q3)
                return view_alloc_work()
            else:
                print("workinggg")
                q5 = "update work set status='workingon' where clerk_id='" + str(a) + "' and work_id='" + str(n) + "'"
                e = db.update(q5)

                q6 = "update  work_report set work_status='" + status + "',description='" + path + "',date=now() where work_id='" + str(n) + "' and cid='"+str(a)+"'"
                res = db.update(q6)
                print("mmmmmmmmmmm", q5,q6)
                return  view_alloc_work()

    else:
            return render_template("login.html")

@app.route('/work_reportpreview/<i>')
def work_reportpreview(i):
    if session['lg'] == "lin":
        q2="select * from work_report where work_id='"+str(i)+"'"
        w=db.selectOne(q2)
        print('mmmmmm',w)
        return  render_template("clerk/wrkpreview.html",d=w)

    else:
            return render_template("login.html")

# clerkend--------------------------------------------------------------------------------------------------------------
# councillor------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------
@app.route('/add_policy')
def add_policy():
    if session['lg'] == "lin":
        return render_template("councillor/addpolicy.html")
    else:
        return render_template("login.html")
@app.route('/add_policy_b',methods=['post'])
def add_policy_b():
    if session['lg'] == "lin":
        pname=request.form['textfield']
        des=request.form['textfield2']
        date=request.form['textfield3']
        a = session['login_id']
        q1="insert into policy(name,councillor_id,description,date,status)values('"+pname+"','"+str(a)+"','"+des+"','"+date+"','pending')"
        r=db.insert(q1)
        return  add_policy()
    else:
        return render_template("login.html")

@app.route('/add_policy_view')
def add_policy_view():
    if session['lg'] == "lin":
        a = session['login_id']
        q1="select * from policy where councillor_id='"+str(a)+"'"
        r=db.select(q1)
        return render_template("councillor/viewpolicy.html",d=r)
    else:
        return render_template("login.html")
@app.route('/add_policy_edit/<d>')
def add_policy_edit(d):
    if session['lg'] == "lin":
        q1 = "select * from policy where policy_id='"+d+"'"
        r = db.selectOne(q1)
        return render_template("councillor/updatepolicy.html",i=r)
    else:
        return render_template("login.html")
@app.route('/add_policy_edit_b',methods=['post'])
def add_policy_edit_b():
    if session['lg'] == "lin":
        pname = request.form['textfield']
        des = request.form['textfield2']
        date = request.form['textfield3']
        a = session['login_id']
        a1="update policy set name='"+pname+"',councillor_id='"+str(a)+"',description='"+des+"',date='"+date+"' where status='pending' and councillor_id='"+str(a)+"'"
        res=db.update(a1)
        return add_policy_view()
    else:
        return render_template("login.html")
@app.route('/add_policy_dlt/<i>')
def add_policy_dlt(i):
    if session['lg'] == "lin":
        q1="delete from policy where policy_id='"+i+"'"
        r=db.delete(q1)
        return add_policy_view()
    else:
        return render_template("login.html")


# ------------------------------------------------------------
@app.route('/add_coordinator')
def add_coordinator():
    if session['lg'] == "lin":
        return render_template("councillor/addcoordinators.html")
    else:
        return render_template("login.html")
@app.route('/add_coordinator_ins',methods=['post'])
def add_coordinator_ins():
    if session['lg'] == "lin":
        name=request.form['textfield']
        gender=request.form['RadioGroup1']
        place=request.form['textfield2']
        post=request.form['textfield3']
        pin=request.form['textfield4']
        email=request.form['textfield5']
        ph=request.form['textfield6']
        pic=request.files['fileField']
        data = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        pic.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\coordinator\\" + data + ".jpg")
        path = "/static/coordinator/" + data + ".jpg"
        print(path)
        q2 = "insert into logintable(username,password,usertype)values('" + email + "','coordinator','coordinator')"
        res = db.insert(q2)
        print("--------------------")
        print(res)
        a = session['login_id']
        print("++++++++++++++")
        print(a)
        q1="insert into coordinator (name,gender,place,post,pin,image,email,phone,login_id,councillor_id,joindate,enddate) values('"+name+"','"+gender+"','"+place+"','"+post+"','"+pin+"','"+path+"','"+email+"','"+ph+"','"+str(res)+"','"+str(a)+"',curdate(),date_add(curdate(),interval 1825 day))"
        res=db.insert(q1)
        return add_coordinator()
    else:
        return render_template("login.html")
@app.route('/add_coordinator_view')
def add_coordinator_view():
    if session['lg'] == "lin":
        q1="select coordinator.*,logintable.*  from coordinator inner join logintable on logintable.login_id=coordinator.login_id where logintable.usertype='coordinator'"
        res=db.select(q1)
        return render_template("councillor/viewcoordinators.html",data=res)
    else:
        return render_template("login.html")
@app.route('/add_coordinator_edit/<i>')
def add_coordinator_edit(i):
    if session['lg'] == "lin":
        q1 = "select * from coordinator where login_id='"+str(i)+"'"

        res=db.selectOne(q1)
        print(res)
        return render_template("councillor/updatecoordinator.html",data=res)
    else:
        return render_template("login.html")

@app.route('/add_coordinator_edit_b',methods=['post'])
def add_coordinator_edit_b():
    if session['lg'] == "lin":
        cid = request.form['cid']
        name = request.form['textfield']
        gender = request.form['RadioGroup1']
        place = request.form['textfield2']
        post = request.form['textfield3']
        pin = request.form['textfield4']
        # email = request.form['textfield5']
        ph = request.form['textfield6']
        pic = request.files['fileField']

        if request.files is not None:
            if pic.filename != "":
                data = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                pic.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\coordinator\\" + data + ".jpg")
                path = "/static/coordinator/" + data + ".jpg"
                print(path)

                q4 = "update coordinator set name='"+name+"',gender='"+gender+"',place='"+place+"',post='"+post+"',pin='"+pin+"',image='"+path+"',phone='"+ph+"' where coordinator_id='"+cid+"'"
                res = db.update(q4)
                return add_coordinator_view()

            else:
                 q5 = "update coordinator set name='"+name+"',gender='"+gender+"',place='"+place+"',post='"+post+"',pin='"+pin+"',phone='"+ph+"' where coordinator_id='"+cid+"'"
                 res = db.update(q5)
                 return add_coordinator_view()
        else:
            q5 = "update coordinator set name='" + name + "',gender='" + gender + "',place='" + place + "',post='" + post + "',pin='" + pin + "',phone='" + ph + "' where coordinator_id='" + cid + "'"
            res = db.update(q5)
            return add_coordinator_view()
    else:
        return render_template("login.html")
@app.route('/add_coordinator_dlt/<i>')
def add_coordinator_dlt(i):
    if session['lg'] == "lin":
        q1="update logintable set usertype='blocked' where login_id='"+i+"'"
        r=db.update(q1)
        return add_coordinator_view()
    else:
        return render_template("login.html")


# ------------------------------------------------------------
@app.route('/add_fund_to_coordinator')
def add_fund_to_coordinator():
    if session['lg'] == "lin":
        q2="select logintable.*,coordinator.* from coordinator inner join logintable on logintable.login_id=coordinator.login_id where logintable.usertype='coordinator' and coordinator.councillor_id='"+str(a)+"'"
        res=db.select(q2)
        a=session['login_id']
        q3 = "select fundalloctocouncillor.*,logintable.* from fundalloctocouncillor inner join  logintable on logintable.login_id=fundalloctocouncillor.mayor_id where logintable.usertype='mayor' and fundalloctocouncillor.councillor_id='"+str(a)+"'"
        w=db.select(q3)
        return render_template("councillor/add_fund_to_coordinator.html",d=res,d2=w)
    else:
        return render_template("login.html")
@app.route('/c',methods=['post'])
def c():
    if session['lg'] == "lin":
        d = session['login_id']
        a=request.form['select']
        b = request.form['select2']
        c=request.form['fund']
        q1="select sum(fund) as s from fundalloctocoodinator where fundids='"+b+"'"
        r=db.selectOne(q1)
        m=r['s']
        print('wwwwwwwwwwwwww',m)
        qry="select fund from fundalloctocouncillor where fund_id='"+b+"'"
        results=db.selectOne(qry)
        f=results['fund']
        if int(c)<=int(f):
            if str(m)=='None':
                q2 = "insert into fundalloctocoodinator(councillor_id,cood_id,date,fund,fundids) values('" + str( d) + "','" + str(a) + "',curdate(),'" + c + "','" + str(b) + "')"
                res = db.insert(q2)
                return add_fund_to_coordinator()
            elif int(m)<int(f):
                q2="insert into fundalloctocoodinator(councillor_id,cood_id,date,fund,fundids) values('"+str(d)+"','"+str(a)+"',curdate(),'"+c+"','"+str(b)+"')"
                res=db.insert(q2)
                return add_fund_to_coordinator()
            else:
                return "<script>alert('you can not allocate the fund');window.location='/add_fund_to_coordinator'</script>"
        else:
            return "<script>alert('you can not allocate the fund');window.location='/add_fund_to_coordinator'</script>"

    else:
        return render_template("login.html")

@app.route('/add_fund_to_coordinator_view')
def add_fund_to_coordinator_view():
    if session['lg'] == "lin":
        a = session['login_id']
        q2="select coordinator.coordinator_id,coordinator.name,coordinator.image,fundalloctocoodinator.* from coordinator inner join fundalloctocoodinator on coordinator.login_id=fundalloctocoodinator.cood_id where fundalloctocoodinator.councillor_id='"+str(a)+"'"
        res=db.select(q2)
        return render_template("councillor/viewfund_to_coordinators.html",d=res)
    else:
        return render_template("login.html")
@app.route('/dltfun/<i>')
def dltfun(i):
    if session['lg'] == "lin":
        q2="delete from fundalloctocoodinator where fund_id='"+str(i)+"'"
        res=db.delete(q2)
        return add_fund_to_coordinator_view()
    else:
        return render_template("login.html")
@app.route('/add_fund_to_coordinator_edit/<i>')
def add_fund_to_coordinator_edit(i):
    if session['lg'] == "lin":
        q2="select logintable.*,coordinator.* from coordinator inner join logintable on logintable.login_id=coordinator.login_id where logintable.usertype='coordinator'"
        res=db.select(q2)
        a=session['login_id']
        q3 = "select fundalloctocouncillor.*,logintable.* from fundalloctocouncillor inner join  logintable on logintable.login_id=fundalloctocouncillor.mayor_id where logintable.usertype='mayor' and fundalloctocouncillor.councillor_id='"+str(a)+"'"
        r=db.select(q3)

        q4 = "select coordinator.coordinator_id,coordinator.name,coordinator.image,fundalloctocoodinator.* from coordinator inner join fundalloctocoodinator on coordinator.login_id=fundalloctocoodinator.cood_id where fundalloctocoodinator.fund_id='"+str(i)+"'"
        res1=db.selectOne(q4)

        return render_template("councillor/update_fund_to_coordinator .html",d=res,d2=r,d3=res1)
    else:
        return render_template("login.html")
@app.route('/b',methods=['post'])
def b():
    if session['lg'] == "lin":
        d = session['login_id']
        a = request.form['select']
        b = request.form['select2']
        c = request.form['fund']
        q2="update fundalloctocoodinator set cood_id='"+a+"',date=curdate(),fund='"+c+"',fundids='"+b+"' where fund_id='"++"'"
        res=db.update(q2)
        return add_fund_to_coordinator_view()
    else:
        return render_template("login.html")

# ------------------------------------------------------------------------
@app.route('/public_need_fund_alloc/<i>')
def public_need_fund_alloc(i):
    if session['lg'] == "lin":
        q2="select publicneedreport.*,publicneedfundalloc.*,coordinator.* from coordinator inner join publicneedreport on coordinator.login_id=publicneedreport.cood_id inner join publicneedfundalloc on publicneedfundalloc.report_id=publicneedreport.report_id where publicneedreport.report_id='"+str(i)+"'"
        res=db.selectOne(q2)
        return render_template("councillor/public_need_fund_allocation.html",d=res)
    else:
        return render_template("login.html")
@app.route('/view_pub_need_report')
def view_pub_need_report():
    if session['lg'] == "lin":
        a=session['login_id']
        q2="select publicneedreport.*,logintable.* from publicneedreport inner join logintable on publicneedreport.cood_id=logintable.login_id inner join coordinator on coordinator.login_id=publicneedreport.cood_id where logintable.usertype='coordinator' and coordinator.councillor_id='"+str(a)+"'"
        res=db.select(q2)
        return render_template("councillor/view_public_need_report.html",d=res)
    else:
        return render_template("login.html")
# ----------------------------------------------------------------------
@app.route('/view_rply')
def view_rply():
    if session['lg'] == "lin":
        a1=session['ward']
        q2="select complaint.*,user.* from user inner join complaint on complaint.from_id=user.login_id where user.ward='"+a1+"'"
        res=db.select(q2)
        return render_template("councillor/view complaints and replay.html",d=res)
    else:
        return render_template("login.html")
@app.route('/sendr/<i>')
def sendr(i):
    if session['lg'] == "lin":
        q2="select complaint,complaint_id from complaint where complaint_id='"+str(i)+"'"
        res=db.selectOne(q2)
        return render_template("councillor/send replay.html",d=res)
    else:
        return render_template("login.html")
@app.route('/send_rply',methods=['post'])
def send_rply():
    if session['lg'] == "lin":
        a=session['login_id']
        rid=request.form['ids']
        rply=request.form['textfield']
        q2="update complaint set reply='"+rply+"',reply_date=curdate(),dept_id='"+str(a)+"' where complaint_id='"+rid+"'"

        res=db.update(q2)
        return view_rply()
    else:
        return render_template("login.html")

# -------------------------------------------------------------------------
@app.route('/view_fund_allocated')
def view_fund_allocated():
    if session['lg'] == "lin":
        return render_template("councillor/viewfundalllocated.html")
    else:
        return render_template("login.html")
# -----------------------------------------------------------------------------

@app.route('/view_cooperation_pro')
def view_cooperation_pro():
    if session['lg'] == "lin":

        q1 = "select * from corporationprofile"
        res = db.select(q1)

        return render_template("councillor/view coorperationprofile.html",data=res)
    else:
        return render_template("login.html")
# -------------------------------------------------------------------------
@app.route('/add_discussion')
def add_discussion():
    if session['lg'] == "lin":
        return render_template("councillor/discussion.html")
    else:
        return render_template("login.html")
@app.route('/add_discussion_b',methods=['post'])
def add_discussion_b():
    if session['lg'] == "lin":
        topic=request.form['textfield']
        date=request.form['textfield1']
        a = session['login_id']
        print("++++++++++++++")
        print(a)
        q1="insert into discussion_forum (from_id,discussion_topic,date) values ('"+str(a)+"','"+topic+"','"+date+"')"
        res=db.insert(q1)
        return add_discussion()
    else:
        return render_template("login.html")
@app.route('/view_discussion')
def view_discussion():
    if session['lg'] == "lin":
        a = session['login_id']
        q1="select * from discussion_forum where from_id='"+str(a)+"' "
        res=db.select(q1)
        return render_template("councillor/viewdiscussion.html",d=res)
    else:
        return render_template("login.html")

@app.route('/view_discussion_more/<i>')
def view_discussion_more(i):
    if session['lg'] == "lin":
        a = session['login_id']
        print("++++++++++++++")
        print(a)
        q2="select discussion_forum.*,discussion_comment.*,count(discussion_comment.topic_id) as a1 from discussion_comment inner join discussion_forum on discussion_comment.topic_id=discussion_forum.discussion_id where discussion_forum.from_id='"+str(a)+"' and discussion_forum.discussion_id='"+str(i)+"'"
        res=db.select(q2)
        print(res)
        q3="select * from discussion_forum where discussion_id='"+str(i)+"'"
        r=db.selectOne(q3)
        print(r)
        return render_template("councillor/discussion_reply.html",d=res,data=r)
    else:
        return render_template("login.html")
@app.route('/moredis/<i>')
def moredis(i):
    if session['lg'] == "lin":
        a = session['login_id']
        b=str(i)
        # print("++++++++++++++")
        # print(a)
        # q2="select discussion_forum.*,discussion_comment.*,user.* from discussion_comment inner join discussion_forum on discussion_comment.topic_id=discussion_forum.discussion_id inner join user on user.user_id=discussion_comment.user_id where discussion_forum.from_id='"+str(a)+"' and discussion_forum.discussion_id='"+str(i)+"'"
        # res=db.select(q2)
        # print(res)
        #
        # q3 = "select discussion_forum.*,discussion_comment.*,user.* from discussion_comment inner join discussion_forum on discussion_comment.topic_id=discussion_forum.discussion_id inner join user on user.user_id=discussion_comment.user_id where discussion_forum.from_id='" + str(a) + "' and discussion_comment.topic_id='" + str(i) + "'"
        # res1 = db.select(q3)
        q2="select discussion_comment.dtype as t,discussion_comment.cdate,discussion_comment.comment,user.name,user.image from discussion_forum as a,discussion_forum as b,discussion_comment,user where a.discussion_id=discussion_comment.topic_id and b.discussion_id=discussion_comment.topic_id and discussion_comment.topic_id and discussion_comment.user_id=user.login_id and discussion_comment.topic_id='"+str(i)+"' and discussion_comment.dtype='user'"
        res=db.select(q2)
        print("bbbbb",res)
        print(b)
        q3 = "select councillor.name as v,councillor.image as i,discussion_comment.dtype as t,discussion_comment.cdate,discussion_comment.comment from discussion_forum as a,discussion_forum as b,discussion_comment,councillor where a.discussion_id=discussion_comment.topic_id and b.discussion_id=discussion_comment.topic_id and discussion_comment.topic_id and discussion_comment.user_id=councillor.login_id and discussion_comment.topic_id='" + str(i) + "' and discussion_comment.dtype='councillor'"
        w = db.select(q3)
        print("n",w)
        return render_template("councillor/disrply2.html",d=res,d2=b,d3=w)
    else:
        return render_template("login.html")
@app.route('/moredisc',methods=['post'])
def moredisc():
    if session['lg'] == "lin":
        a = session['login_id']
        m=request.form['m']
        n=request.form['n']
        q2="insert into discussion_comment(topic_id,user_id,comment,cdate,dtype) values('"+m+"','"+str(a)+"','"+n+"',now(),'councillor') "
        res=db.insert(q2)
        return view_discussion()
    else:
        return render_template("login.html")
# ---------------------------------------------------------------------------
@app.route('/view_meeting')
def view_meeting():
    if session['lg'] == "lin":

        q2="select meeting.*,logintable.* from logintable inner join meeting on meeting.mayorid=logintable.login_id where logintable.usertype='mayor'"
        res=db.select(q2)
        return render_template("councillor/viewmeeting.html",d=res)
    else:
        return render_template("login.html")
# ------------------------------------------------------------------------------
@app.route('/view_notifi')
def view_notifi():
    if session['lg'] == "lin":
        a = session['login_id']
        q2 = "select notification.*,logintable.* from logintable inner join notification on logintable.login_id=notification.mayor_id where logintable.usertype='mayor'"
        res = db.select(q2)
        return render_template("councillor/viewnotification.html",data=res)
    else:
        return render_template("login.html")

# ===============================================================================
@app.route('/view_sugg')
def view_sugg():
    if session['lg'] == "lin":

        q2="select suggestion.*,user.* from suggestion inner join user on suggestion.user_id=user.login_id"
        res=db.select(q2)
        return render_template("councillor/viewsuggestion.html",d=res)
    else:
        return render_template("login.html")
# -----------------------------------------------------------------------------
@app.route('/view_services')
def view_services():
    if session['lg'] == "lin":

        q2="select service.*,logintable.* from logintable inner join service on  service.m_id=logintable.login_id where usertype='mayor'"
        res=db.select(q2)
        return render_template("councillor/view service.html",d=res)
    else:
        return render_template("login.html")
# -----------------------------------------------------------
@app.route('/view_rating')
def view_rating():
    if session['lg'] == "lin":

        a = session['login_id']
        print('mmm',a)
        q1="select councillorrating.*,user.* from councillorrating join user on user.login_id=councillorrating.user_id where councillorrating.councillor_id='"+str(a)+"'"
        res=db.select(q1)
        print(res)
        return render_template("councillor/viewrating.html",data=res)
    else:
        return render_template("login.html")
# =================================================================
@app.route('/chat_councillors')
def chat_councillors():
    if session['lg'] == "lin":
        return render_template("councillor/interaction/councillor_to_councillor_chat.html")
    else:
        return render_template("login.html")
@app.route('/councillor_chats',methods=['post'])
def councillor_chats():
    if session['lg'] == "lin":
        a=session['login_id']
        q1 = "select councillor.*,logintable.login_id as i,logintable.usertype from councillor inner join logintable on logintable.login_id=councillor.login_id where councillor.login_id!='"+str(a)+"' and logintable.usertype='councillors'"
        res = db.select(q1)
        v={}
        if len(res)>0:
            v["status"]="ok"
            v['data']=res
        else:
            v["status"]="error"

        rw=demjson.encode(v)
        print(rw)
        return rw
    else:
        return render_template("login.html")

@app.route('/chatsndctoc', methods=['post'])
def chatsndctoc():
        if session['lg'] == "lin":
            c = session['login_id']
            b = request.form['n']
            print(b)
            m = request.form['m']

            q2 = "insert into councillorconcillorchat(from_id,to_id,messege,date) values('" + str(c) + "','" + str( b) + "','" + m + "',curdate())"
            res = db.insert(q2)
            v = {}
            if int(res) > 0:
                v["status"] = "ok"

            else:
                v["status"] = "error"

            r = demjson.encode(v)

            return r
        else:
            return render_template("login.html")

@app.route('/chatrplyctoc', methods=['post'])
def chatrplyctoc():
    if session['lg'] == "lin":
        print("...........................")
        c = session['login_id']
        b = request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from councillorconcillorchat ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id'] = c
        else:
            v["status"] = "error"
        rw = demjson.encode(v)
        return rw
    else:
        return render_template("login.html")
# ===============================================================================================

@app.route('/chat_mayor')
def chat_mayor():
    return render_template("councillor/interaction/councillor_to_mayor_chat.html")
@app.route('/councillor_chatsctom',methods=['post'])
def councillor_chatsctom():
    if session['lg'] == "lin":
        a=session['login_id']
        q1="select mayor.*,logintable.login_id as i,logintable.usertype from mayor inner join logintable on logintable.login_id=mayor.login_id where logintable.usertype='mayor'"
        res = db.select(q1)
        v={}
        if len(res)>0:
            v["status"]="ok"
            v['data']=res
        else:
            v["status"]="error"

        rw=demjson.encode(v)
        print(rw)
        return rw
    else:
        return render_template("login.html")

@app.route('/chatsndctom', methods=['post'])
def chatsndctom():
        if session['lg'] == "lin":
            c = session['login_id']
            b = request.form['n']
            print(b)
            m = request.form['m']

            q2 = "insert into councillormayorchat(from_id,to_id,messege,date) values('" + str(c) + "','" + str( b) + "','" + m + "',curdate())"
            res = db.insert(q2)
            v = {}
            if int(res) > 0:
                v["status"] = "ok"

            else:
                v["status"] = "error"

            r = demjson.encode(v)

            return r
        else:
            return render_template("login.html")

@app.route('/chatrplyctom', methods=['post'])
def chatrplyctom():
    if session['lg'] == "lin":
        print("...........................")
        c = session['login_id']
        b = request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from councillormayorchat ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id'] = c
        else:
            v["status"] = "error"
        rw = demjson.encode(v)
        return rw
    else:
        return render_template("login.html")
#======================================================================================

@app.route('/chat_coordinators')
def chat_coordinators():
    return render_template("councillor/interaction/councillor_to_coordindtor_chat.html")

@app.route('/councillor_chatsctoco', methods=['post'])
def councillor_chatsctoco():
    if session['lg'] == "lin":
        a = session['login_id']
        q1 = "select coordinator.*,logintable.login_id as i,logintable.usertype from coordinator inner join logintable on logintable.login_id=coordinator.login_id where logintable.usertype='coordinator'"
        res = db.select(q1)
        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        print(rw)
        return rw
    else:
        return render_template("login.html")

@app.route('/chatsndctoco', methods=['post'])
def chatsndctoco():
    if session['lg'] == "lin":
        c = session['login_id']
        b = request.form['n']
        print(b)
        m = request.form['m']

        q2 = "insert into councillorcoodchat(from_id,to_id,messege,date) values('" + str(c) + "','" + str( b) + "','" + m + "',curdate())"
        res = db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r
    else:
        return render_template("login.html")

@app.route('/chatrplyctoco', methods=['post'])
def chatrplyctoco():
    if session['lg'] == "lin":
        print("...........................")
        c = session['login_id']
        b = request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from councillorcoodchat ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id'] = c
        else:
            v["status"] = "error"
        rw = demjson.encode(v)
        return rw
    else:
        return render_template("login.html")

# councillorend---------------------------------------------------------------------------------------------------------

# user--------------------------------------------------------------------------------------------------------------------






if __name__ == '__main__':
    app.run(debug=True)