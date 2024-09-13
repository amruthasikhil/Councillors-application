package com.example.user.councillorsappand;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class Usersendsuggestion extends AppCompatActivity implements View.OnClickListener {
    EditText e1;

    Button b1, b2;
    String suggestion;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );
        setContentView( R.layout.activity_usersendsuggestion );
        e1 = (EditText) findViewById( R.id.editText );
        b1 = (Button) findViewById( R.id.button );
        b2 = (Button) findViewById( R.id.button2 );
        b1.setOnClickListener( this );
        b2.setOnClickListener( this );
    }

    @Override
    public void onClick(View view) {
        if (view == b2) {
            Intent ij = new Intent( getApplicationContext(), Usersendsuggestion.class );
            startActivity( ij );
        }
        if (view == b1) {
            int flag=0;
            suggestion = e1.getText().toString();
            if(suggestion.equalsIgnoreCase( "" )) {
                e1.setError( "*" );
                flag++;
            }
            if(flag==0){
            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences( getApplicationContext() );

            String hu = sh.getString( "ip", "" );
            String url = "http://" + hu + ":5000/and_usersuggestionsend";


            RequestQueue requestQueue = Volley.newRequestQueue( getApplicationContext() );
            StringRequest postRequest = new StringRequest( Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
//                            Toast.makeText( getApplicationContext(), response, Toast.LENGTH_LONG ).show();

                            // response
                            try {
                                JSONObject jsonObj = new JSONObject( response );
                                if (jsonObj.getString( "status" ).equalsIgnoreCase( "Inserted" )) {

                                    startActivity( new Intent( getApplicationContext(), Usersuggestion.class ) );

                                }


                                // }
                                else {
                                    Toast.makeText( getApplicationContext(), "Not found", Toast.LENGTH_LONG ).show();
                                }

                            } catch (Exception e) {
                                Toast.makeText( getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT ).show();
                            }
                        }
                    },
                    new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            // error
                            Toast.makeText( getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT ).show();
                        }
                    }
            ) {
                @Override
                protected Map<String, String> getParams() {
                    SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences( getApplicationContext() );
                    Map<String, String> params = new HashMap<String, String>();

                    String id = sh.getString( "logid", "" );
                    params.put( "uid", id );
                    params.put( "sug", suggestion );
//                params.put("mac",maclis);

                    return params;
                }
            };

            int MY_SOCKET_TIMEOUT_MS = 100000;

            postRequest.setRetryPolicy( new DefaultRetryPolicy(
                    MY_SOCKET_TIMEOUT_MS,
                    DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                    DefaultRetryPolicy.DEFAULT_BACKOFF_MULT ) );
            requestQueue.add( postRequest );

        }}
    }
}