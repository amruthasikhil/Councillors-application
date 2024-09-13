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

public class custom_userdiscussionview extends BaseAdapter{
    String[] topic1,date1,imag1,disid1;
    private Context context;
    public custom_userdiscussionview(Context applicationContext, String[] topic, String[] date, String[] image, String[] disid) {
        this.context=applicationContext;
        this.topic1=topic;
        this.date1=date;
        this.imag1=image;
        this.disid1=disid;

    }

    @Override
    public int getCount() {
        return topic1.length;
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
            gridView=inflator.inflate(R.layout.custom_userdisscussionview,null);//same class name

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView12);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView22);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView53);
        ImageView im=(ImageView) gridView.findViewById(R.id.image );
        tv1.setTextColor( Color.BLACK);//color setting
        tv2.setTextColor(Color.BLACK);
        tv3.setTextColor(Color.BLACK);
        tv3.setOnClickListener( new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SharedPreferences sh1= PreferenceManager.getDefaultSharedPreferences(context);
                SharedPreferences.Editor e1=sh1.edit();
                e1.putString( "disid",disid1[i] );
                e1.commit();
                //in the case of custom page the intent
                Intent ij=new Intent(context,Userdisccussionsend.class);
                ij.setFlags( Intent.FLAG_ACTIVITY_NEW_TASK );
                context.startActivity(ij);
            }
        } );





//        tv1.setText(user[]);//for serial no
        tv1.setText(topic1[i]);
        tv2.setText(date1[i]);

        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String ip=sh.getString("ip","");
        String url="http://" + ip + ":5000"+imag1[i];
        Picasso.with(context).load(url).transform(new CircleTransform()). into(im);//circle





        return gridView;
    }
}
