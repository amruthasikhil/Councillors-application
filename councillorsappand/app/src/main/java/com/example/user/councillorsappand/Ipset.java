package com.example.user.councillorsappand;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Ipset extends AppCompatActivity implements View.OnClickListener {
    EditText e1;
    Button b1,b2;
    String ipadrs,url;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ipset);
        e1=(EditText)findViewById(R.id.edreview);
        b1=(Button)findViewById(R.id.bt1);
        b2=(Button)findViewById(R.id.bt2);
        b1.setOnClickListener(this);
        b2.setOnClickListener(this);
        sh= PreferenceManager.getDefaultSharedPreferences( getApplicationContext() );
        e1.setText(sh.getString("ip",""));

    }

    @Override
    public void onClick(View view) {
        if(view==b1)

        {
            ipadrs=e1.getText().toString();
            url="http://"+ipadrs+"5000/";
            SharedPreferences.Editor e=sh.edit();
            e.putString( "ip",ipadrs );
            e.putString( "url1",url );
            e.commit();
            Intent i = new Intent( getApplicationContext(),MainActivity.class );
            startActivity( i );




        }
        if(view==b2){
            Intent i=new Intent(getApplicationContext(),Ipset.class);
            startActivity( i );

        }

    }


}
