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

public class custom_fundallocationcoordinator extends BaseAdapter{
    private Context context;
    String[] cname1,fund1,photo1,date1;
    public custom_fundallocationcoordinator(Context applicationContext, String[] cname, String[] fund, String[] photo, String[] date) {
    this.context=applicationContext;
    this.cname1=cname;
    this.date1=date;
    this.fund1=fund;
    this.photo1=photo;

    }

    @Override
    public int getCount() {
        return cname1.length;
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
            gridView=inflator.inflate(R.layout.custom_fundallocationcoordinator,null);//same class name

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView70);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView74);
        ImageView im=(ImageView) gridView.findViewById(R.id.image);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView78);
//
        tv1.setTextColor( Color.BLACK);//color setting
        tv2.setTextColor(Color.BLACK);
        tv3.setTextColor(Color.BLACK);
        tv1.setText(cname1[i]);
        tv2.setText(date1[i]);
        tv3.setText(fund1[i]);
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String ip=sh.getString("ip","");
        String url="http://" + ip + ":5000"+photo1[i];
        Picasso.with(context).load(url).transform(new CircleTransform()). into(im);//circle
//




        return gridView;

    }
}
