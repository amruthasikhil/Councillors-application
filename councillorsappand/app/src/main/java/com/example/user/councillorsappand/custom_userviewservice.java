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

public class custom_userviewservice extends BaseAdapter {
    String[] name1,des;
    private Context context;
    public custom_userviewservice(Context applicationContext, String[] name, String[] description) {
        this.context=applicationContext;
        this.name1=name;
        this.des=description;

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
            gridView=inflator.inflate(R.layout.custom_userviewservice,null);//same class name

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView17);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView18);
//        ImageView im=(ImageView) gridView.findViewById(R.id.imageView5);
//        TextView tv3=(TextView)gridView.findViewById(R.id.textView13);
//        TextView tv4=(TextView)gridView.findViewById(R.id. textView10);
//        TextView tv5=(TextView)gridView.findViewById(R.id. textView11);


        tv1.setTextColor( Color.BLACK);//color setting
        tv2.setTextColor(Color.BLACK);
//        tv3.setTextColor(Color.BLACK);




//        tv1.setText(user[]);//for serial no
        tv1.setText(name1[i]);
        tv2.setText(des[i]);
//        tv3.setText(period3[i]);
//        tv4.setText(email1[i]);
//        tv5.setText(phone1[i]);

//        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
//        String ip=sh.getString("ip","");
//        String url="http://" + ip + ":5000"+photo1[i];
//        Picasso.with(context).load(url).transform(new CircleTransform()). into(im);//circle
//




        return gridView;

    }
}
