package com.example.user.councillorsappand;

import android.content.Context;
import android.graphics.Color;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

public class custom_usersuggestion extends BaseAdapter{
    String[] suggestion1,dat1;
    private  Context context;
    public custom_usersuggestion(Context applicationContext, String[] suggestion, String[] date) {
        this.context=applicationContext;
        this.suggestion1=suggestion;
        this.dat1=date;

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
            gridView=inflator.inflate(R.layout.custom_usersuggestion,null);//same class name

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView45);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView47);

        tv1.setTextColor( Color.BLACK);//color setting
        tv2.setTextColor( Color.BLACK);

        tv1.setText(suggestion1[i]);
        tv2.setText(dat1[i]);

        return gridView;
    }
}
