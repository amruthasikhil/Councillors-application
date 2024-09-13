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

public class custom_userprojectview extends BaseAdapter {
    String[] name1,details1,photo1,pid1;
    private Context context;
    public custom_userprojectview(Context applicationContext, String[] name, String[] details, String[] Photo,String[] pid) {
    this.context=applicationContext;
    this.name1=name;
    this.details1=details;
    this.photo1=Photo;
    this.pid1=pid;

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
    public View getView(final int i, View view, ViewGroup viewGroup) {
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);


        View gridView;
        if(view==null)
        {
            gridView=new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView=inflator.inflate(R.layout.custom_userprojectview,null);//same class name

        }
        else
        {
            gridView=(View)view;

        }
        TextView t1=(TextView)gridView.findViewById( R.id.textView28);
        TextView t2=(TextView)gridView.findViewById( R.id.textView27);
//        TextView t3=(TextView)gridView.findViewById( R.id.textView20);
//        TextView t3=(TextView)gridView.findViewById( R.id.textView23);
        TextView t4=(TextView)gridView.findViewById( R.id.textView30);
        t4.setOnClickListener( new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SharedPreferences sh1= PreferenceManager.getDefaultSharedPreferences(context);
                SharedPreferences.Editor e1=sh1.edit();
                e1.putString( "proid",pid1[i] );
                e1.commit();
                //in the case of custom page the intent
                Intent ij=new Intent(context,Userprojectmore.class);
                ij.setFlags( Intent.FLAG_ACTIVITY_NEW_TASK );
                context.startActivity(ij);
            }
        } );
        ImageView im=(ImageView)gridView.findViewById( R.id.imageView7);


        t1.setTextColor( Color.BLACK);//color setting
        t2.setTextColor(Color.BLACK);
//        t3.setTextColor(Color.BLACK);
//        t4.setTextColor(Color.BLACK);
//        t5.setTextColor(Color.BLACK);

        t1.setText(name1[i]);
        t2.setText(details1[i]);
//        t3.setText([i]);
//        t4.setText(date1[i]);
//        t5.setText(phone1[i]);
//
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String ip=sh.getString("ip","");
        String url="http://" + ip + ":5000"+photo1[i];
        Picasso.with(context).load(url).transform(new CircleTransform()). into(im);//circle
        return gridView;

    }


}
