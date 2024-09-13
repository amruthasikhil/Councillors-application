package com.example.user.councillorsappand;

import android.content.Context;
import android.content.Intent;
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

public class custom_userdiscussionsend extends BaseAdapter{
    String[] image1,comment1,name1;
    private Context context;
    public custom_userdiscussionsend(Context applicationContext, String[] image, String[] comment, String[] name) {
    this.context=applicationContext;
    this.image1=image;
    this.comment1=comment;
    this.name1=name;
    }

    @Override
    public int getCount() {
        return name1.length;
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
            gridView=inflator.inflate(R.layout.custom_userdiscussionsend,null);//same class name

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView56);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView57);
        ImageView im=(ImageView) gridView.findViewById(R.id.imageView8);
        tv1.setTextColor( Color.BLACK);//color setting
        tv2.setTextColor(Color.BLACK);






//        tv1.setText(user[]);//for serial no
        tv1.setText(comment1[i]);
        tv2.setText(name1[i]);

        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String ip=sh.getString("ip","");
        String url="http://" + ip + ":5000"+image1[i];
        Picasso.with(context).load(url).transform(new CircleTransform()). into(im);//circle





        return gridView;
    }
}
