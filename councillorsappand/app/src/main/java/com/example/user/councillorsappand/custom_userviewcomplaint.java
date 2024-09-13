package com.example.user.councillorsappand;

import android.content.Context;
import android.graphics.Color;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

public class custom_userviewcomplaint extends BaseAdapter{
    String[] complaint1,dat1,dat2,reply;
    private  Context context;
    public custom_userviewcomplaint(Context applicationContext, String[] complaint, String[] date, String[] rply, String[] todate) {
        this.context=applicationContext;
        this.complaint1=complaint;
        this.dat1=date;
        this.reply=rply;
        this.dat2=todate;
    }

    @Override
    public int getCount() {
        return dat1.length;
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
//            gridView=inflator.inflate(R.layout.custom_userviewcomplaint, null);
            gridView=inflator.inflate(R.layout.custom_userviewcomplaint,null);//same class name

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView45);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView47);
////
        TextView tv3=(TextView)gridView.findViewById(R.id.textView49);
        TextView tv4=(TextView)gridView.findViewById(R.id. textView51);
////        TextView tv5=(TextView)gridView.findViewById(R.id. textView11);


        tv1.setTextColor( Color.BLACK);//color setting
        tv2.setTextColor( Color.BLACK);
        tv3.setTextColor(Color.BLACK);
        tv4.setTextColor(Color.BLACK);




//        tv1.setText(user[]);//for serial no
        tv1.setText(complaint1[i]);
        tv2.setText(dat1[i]);
        tv3.setText(reply[i]);
        tv4.setText(dat2[i]);

        return gridView;
    }
}
