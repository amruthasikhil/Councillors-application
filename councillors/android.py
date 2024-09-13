from flask import Flask, render_template, request, session, jsonify, redirect
import demjson
from DBConnection import Db
import datetime
db=Db()
app = Flask(__name__)
app.secret_key="nnn"
# user--------------------------------------------------------------------------------------------------------------------

@app.route('/and_login',methods=['post'])
def and_login():
    usr = request.form['username']
    passwd = request.form['passwd']

    qry = "select * from logintable where username='" + usr + "'and password='" + passwd + "'"
    res = db.selectOne(qry)
    res1 = {}
    if res != None:
        type = res['usertype']
        print(type)
        if type == "admin":
            res1['status'] = "none"
            return demjson.encode(res1)
        else:
            id = res['login_id']
            res1['status'] = 'ok'
            res1['type1'] = type
            res1['id1'] = id

            return demjson.encode(res1)
    else:
        res1['status'] = 'none'
        return demjson.encode(res1)
@app.route('/user_registration',methods=['post'])
def user_registration():
    name=request.form['name']
    place=request.form['place']
    post=request.form['post']
    pin=request.form['pin']
    email=request.form['email']
    pno=request.form['phone']
    ward=request.form['ward']
    password=request.form['password']
    cpass=request.form['cpass']
    image=request.files['pic']
    if password==cpass:
        q3="insert into logintable(username,password,usertype) values('"+email+"','"+password+"','user')"
        lid=db.insert(q3)
        extn = image.filename.split(".")[-1]
        user_pic = "user_" + str(lid) + "." + extn
        image.save("C:\\Users\\user\\PycharmProjects\\councillors\\static\\user\\" + user_pic)
        path = "/static/user/" + user_pic
        q2="insert into user(name,login_id,place,post,pin,phone,email,ward,image) values('"+name+"','"+str(lid)+"','"+place+"','"+post+"','"+pin+"','"+pno+"','"+email+"','"+ward+"','"+path+"')"
        res=db.insert(q2)
        res1={}
        res1['status']="ok"
        return demjson.encode(res1)
    else:
        res1 = {}
        res1['status'] = "error"
        return demjson.encode(res1)
@app.route('/uprofile',methods=['post'])
def uprofile():
    lid=request.form['uid']
    q2="select * from user where login_id='"+str(lid)+"'"
    res=db.selectOne(q2)
    res1={}
    res1['status']="ok"
    res1['data']=res
    return  demjson.encode(res1)
@app.route('/coordinatorprofile',methods=['post'])
def coordinatorprofile():
    lid = request.form['uid']
    q2 = "select * from coordinator where login_id='" + str(lid) + "'"
    res = db.selectOne(q2)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_coorperationprofile',methods=['post'])
def and_coorperationprofile():
    lid = request.form['uid']
    q2="select * from corporationprofile"
    res = db.selectOne(q2)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_mayorview',methods=['post'])
def and_mayorview():
    q3 = "select logintable.*,mayor.* from mayor inner join logintable on logintable.login_id=mayor.login_id where logintable.usertype='mayor'"
    res = db.selectOne(q3)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_mayorviewold',methods=['post'])
def and_mayorviewold():
    q3 = "select logintable.*,mayor.* from mayor inner join logintable on logintable.login_id=mayor.login_id where logintable.usertype='blocked'"
    res = db.select(q3)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)

@app.route('/and_userserviceview',methods=['post'])
def and_userserviceview():
    q2 = "select service.*,logintable.* from logintable inner join service on  service.m_id=logintable.login_id where usertype='mayor'"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_usernotification',methods=['post'])
def and_usernotification():
    q2 = "select notification.*,logintable.*,mayor.login_id,mayor.picture from logintable inner join notification on logintable.login_id=notification.mayor_id  inner join mayor on mayor.login_id=notification.mayor_id where logintable.usertype='mayor'"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_userpolicyview',methods=['post'])
def and_userpolicyview():
    usid = request.form['uid']
    q3 = "select * from user where login_id='" + str(usid) + "'"
    re = db.selectOne(q3)
    ward1 = re['ward']
    q2="select policy.*,logintable.*,councillor.login_id,councillor.name as v,councillor.image,councillor.ward from logintable inner join policy on policy.councillor_id=logintable.login_id inner join councillor on councillor.login_id=policy.councillor_id where logintable.usertype='councillors' and policy.status='accept' and councillor.ward='"+ward1+"'"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_userprojectview',methods=['post'])
def and_userprojectview():
    q2="select project.*,logintable.*,mayor.login_id,mayor.picture from logintable inner join project on project.uid=logintable.login_id inner join mayor on mayor.login_id=project.uid where logintable.usertype='mayor' and project.status='Complete'"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_userprojectviewmore',methods=['post'])
def and_userprojectviewmore():
    a=request.form['pid']
    q2="select project.*,logintable.*,mayor.login_id,mayor.picture from logintable inner join project on project.uid=logintable.login_id inner join mayor on mayor.login_id=project.uid where logintable.usertype='mayor' and project.status='Complete' and project.project_id='"+str(a)+"'"
    res = db.selectOne(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_addcomplaints',methods=['post'])
def and_addcomplaints():
    a=request.form['uid']
    print(';;;',a)
    q2="select * from complaint where from_id='"+str(a)+"'"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_sendcomplaints',methods=['post'])
def and_sendcomplaints():
    usid = request.form['uid']
    cmpt = request.form['cmpt']
    q2="insert complaint(complaint,complaint_date,from_id,reply,reply_date,dept_id) values('"+cmpt+"',curdate(),'"+str(usid)+"','pending','pending','pending')"
    res=db.insert(q2)
    res1={}
    res1['status']="Inserted"
    return demjson.encode(res1)
@app.route('/and_usersuggestion',methods=['post'])
def and_usersuggestion():
    usid = request.form['uid']
    q2="select * from suggestion where user_id='"+str(usid)+"'"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_usersuggestionsend',methods=['post'])
def and_usersuggestionsend():
    usid = request.form['uid']
    cmpt = request.form['sug']
    q2="insert into suggestion(suggestion,date,user_id) values('"+cmpt+"',curdate(),'"+str(usid)+"')"
    res = db.insert(q2)
    res1 = {}
    res1['status'] = "Inserted"
    return demjson.encode(res1)
@app.route('/and_dept',methods=['post'])
def and_dept():
    # usid = request.form['uid']
    q2="select * from dept"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_insertdeptrating',methods=['post'])
def and_insertdeptrating():
    usid = request.form['uid']
    rate = request.form['rating']
    did=request.form['did']
    q2="insert into departmentrating(dept_id,user_id,rating,date) values('"+str(did)+"','"+str(usid)+"','"+rate+"',curdate())"
    res = db.insert(q2)
    res1 = {}
    res1['status'] = "Inserted"
    return demjson.encode(res1)
@app.route('/and_councillor',methods=['post'])
def and_councillor():
    # usid = request.form['uid']
    q2="select * from councillor"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_insertcouncillor',methods=['post'])
def and_insertcouncillor():
    usid = request.form['uid']
    rate = request.form['rating']
    did=request.form['did']
    q2="insert into councillorrating(councillor_id,user_id,rating,date) values('"+str(did)+"','"+str(usid)+"','"+rate+"',curdate())"
    res = db.insert(q2)
    res1 = {}
    res1['status'] = "Inserted"
    return demjson.encode(res1)
@app.route('/and_discussion',methods=['post'])
def and_discussion():
    usid = request.form['uid']
    q3="select * from user where login_id='"+str(usid)+"'"
    re=db.selectOne(q3)
    ward1=re['ward']
    q2="select discussion_forum.*,councillor.* ,logintable.* from discussion_forum inner join councillor on discussion_forum.from_id=councillor.login_id inner join logintable on logintable.login_id=councillor.login_id where logintable.usertype='councillors' and councillor.ward='"+str(ward1)+"'"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_discussionview',methods=['post'])
def and_discussionview():
    did = request.form['did']
    print(did)
    q2="select * from discussion  where topic_id='"+str(did)+"' order by comment_id"
    res = db.select(q2)
    print(res)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_discussioninsert',methods=['post'])
def and_discussioninsert():
    usid = request.form['uid']
    did = request.form['did']
    comment = request.form['comment']
    print(usid,did,comment)
    q2="insert into discussion_comment(topic_id,user_id,comment,cdate,dtype) values('"+str(did)+"','"+str(usid)+"','"+comment+"',now(),'user')"
    res = db.insert(q2)
    res1 = {}
    res1['status'] = "Inserted"
    return demjson.encode(res1)
@app.route('/and_coordinatorcouncillor',methods=['post'])
def and_coordinatorcouncillor():
    q2="select councillor.*from coordinator inner join councillor on councillor.login_id=coordinator.councillor_id group by councillor_id"
    res = db.selectOne(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/and_coordpolicyview',methods=['post'])
def and_coordpolicyview():
    q2="select policy.*,councillor.name as v,councillor.image from councillor inner join policy on policy.councillor_id=councillor.login_id where policy.status='accept'"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)

@app.route('/add_chat',methods=['post'])
def add_chat():
    lid = request.form['lid']
    toid = request.form['toid']
    message = request.form['message']
    q2="insert into councillorcoodchat(from_id,to_id,messege,date)values('"+lid+"','"+toid+"','"+message+"',curdate())"
    res = db.insert(q2)
    res1 = {}
    res1['status'] = "Inserted"
    return demjson.encode(res1)

@app.route('/view_chat',methods=['post'])
def view_chat():
    lid = request.form['lid']
    toid = request.form['toid']
    lastid = request.form['lastid']
    print(lid,toid,lastid)
    q2="select councillorcoodchat.* from councillorcoodchat where chat_id>'"+lastid+"' and ((from_id='"+lid+"' and to_id='"+toid+"') or (from_id='"+toid+"' and to_id='"+lid+"'))"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/view_chatcouncillor',methods=['post'])
def view_chatcouncillor():
    q2="select councillor.* from councillor inner join coordinator on coordinator.councillor_id=councillor.login_id group by councillor_id"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)


@app.route('/and_coodfundview',methods=['post'])
def and_coodfundview():
    usid = request.form['uid']
    q2="select councillor.*,fundalloctocoodinator.* from councillor inner join fundalloctocoodinator on fundalloctocoodinator.councillor_id=councillor.login_id inner join coordinator on coordinator.login_id=fundalloctocoodinator.cood_id inner join logintable on logintable.login_id=coordinator.login_id where coordinator.login_id='"+usid+"'"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)

if __name__ == '__main__':
    app.run(host="0.0.0.0")