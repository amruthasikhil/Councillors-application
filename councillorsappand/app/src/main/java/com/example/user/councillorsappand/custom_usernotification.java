package com.example.user.councillorsappand;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

public class custom_usernotification extends BaseAdapter{
    String[] sub1,des1,date1,photo1;
    private Context context;
    public custom_usernotification(Context applicationContext, String[] sub, String[] des, String[] date, String[] photo) {
    this.context=applicationContext;
    this.sub1=sub;
    this.des1=des;
    this.date1=date;
    this.photo1=photo;
    }

    @Override
    public int getCount() {
        return sub1.length;
    }

    @Override
    public Object getItem(int i) {
        return null;
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(view==null)
        {
            gridView=new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView=inflator.inflate(R.layout.custom_usernotification,null);//same class name

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView12);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView22);
        ImageView im=(ImageView) gridView.findViewById(R.id.image );
//        TextView tv3=(TextView)gridView.findViewById(R.id.textView13);
//        TextView tv4=(TextView)gridView.findViewById(R.id. textView10);
        TextView tv5=(TextView)gridView.findViewById(R.id. textView11);


        tv1.setTextColor( Color.BLACK);//color setting
        tv2.setTextColor(Color.BLACK);
        tv5.setTextColor(Color.BLACK);




//        tv1.setText(user[]);//for serial no
        tv1.setText(sub1[i]);
        tv2.setText(des1[i]);
//        tv3.setText(period3[i]);
//        tv4.setText(email1[i]);
        tv5.setText(date1[i]);

        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String ip=sh.getString("ip","");
        String url="http://" + ip + ":5000"+photo1[i];
        Picasso.with(context).load(url).transform(new CircleTransform()). into(im);//circle





        return gridView;

    }
}
