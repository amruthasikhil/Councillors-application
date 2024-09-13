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
import android.widget.ListView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

public class custom_userpolicyview extends BaseAdapter{
    String[] pname1,councillorname1,des1,date1,photo1;
    private Context context;

    public custom_userpolicyview(Context applicationContext, String[] pname, String[] councillorname, String[] des, String[] photo, String[] date) {
        this.context=applicationContext;
        this.pname1=pname;
        this.councillorname1=councillorname;
        this.des1=des;
        this.date1=date;
        this.photo1=photo;
    }

    @Override
    public int getCount() {
        return pname1.length;
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
            gridView=inflator.inflate(R.layout.custom_userpolicyview,null);//same class name

        }
        else
        {
            gridView=(View)view;

        }
        TextView t1=(TextView)gridView.findViewById( R.id.textView15);
        TextView t2=(TextView)gridView.findViewById( R.id.textView19);
//        TextView t3=(TextView)gridView.findViewById( R.id.textView20);
        TextView t3=(TextView)gridView.findViewById( R.id.textView23);
        TextView t4=(TextView)gridView.findViewById( R.id.textView25);
        ImageView im=(ImageView)gridView.findViewById( R.id.imageView6);


        t1.setTextColor( Color.BLACK);//color setting
        t2.setTextColor(Color.BLACK);
        t3.setTextColor(Color.BLACK);
        t4.setTextColor(Color.BLACK);
//        t5.setTextColor(Color.BLACK);

        t2.setText(pname1[i]);
        t1.setText(councillorname1[i]);
        t3.setText(des1[i]);
        t4.setText(date1[i]);
//        t5.setText(phone1[i]);
//
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String ip=sh.getString("ip","");
        String url="http://" + ip + ":5000"+photo1[i];
        Picasso.with(context).load(url).transform(new CircleTransform()). into(im);//circle
        return gridView;

    }
}
