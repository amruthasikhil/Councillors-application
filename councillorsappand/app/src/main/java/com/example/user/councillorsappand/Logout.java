package com.example.user.councillorsappand;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class Logout extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );
        setContentView( R.layout.activity_logout );
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences( this );
        SharedPreferences.Editor ed=sh.edit();
        ed.clear();
        ed.commit();

        Intent ij=new Intent( getApplicationContext(),Ipset.class );
        startActivity( ij );

    }
}
