package com.example.user.councillorsappand;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.RatingBar;
import android.widget.Spinner;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class Councillorrating extends AppCompatActivity implements View.OnClickListener, AdapterView.OnItemSelectedListener {
    RatingBar r1;
    Button b1;
    Spinner select;
    String[] did,cname;
    String did1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );
        setContentView( R.layout.activity_councillorrating );
        r1=(RatingBar)findViewById( R.id.ratingBar );
        b1=(Button)findViewById( R.id.button );
        select=(Spinner)findViewById( R.id.spinner );
        b1.setOnClickListener( this );
        select.setOnItemSelectedListener( this );
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        String hu = sh.getString("ip", "");
        String url = "http://" + hu + ":5000/and_councillor";



        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        StringRequest postRequest = new StringRequest( Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
//                            Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();

                        // response
                        try {
                            JSONObject jsonObj = new JSONObject(response);
                            if (jsonObj.getString("status").equalsIgnoreCase("ok")) {
//view service code
                                JSONArray js = jsonObj.getJSONArray( "data" );//from python
                                did = new String[js.length()];
                                cname = new String[js.length()];
//

//                                JSONArray js1= jsonObj.getJSONArray("rating");
//                                rating=new String[js1.length()];

                                for (int i = 0; i < js.length(); i++) {
                                    JSONObject u = js.getJSONObject( i );
                                    did[i] = u.getString( "login_id" );//dbcolumn name
                                    cname[i] = u.getString( "name" );

                                }
//                                for(int i=0;i<js1.length();i++)
//                                {
//                                    JSONObject u=js1.getJSONObject(i);
//                                    rating[i]=u.getString("rating");
//
//                                }

                                ArrayAdapter<String> adpt = new ArrayAdapter<String>( getApplicationContext(), android.R.layout.simple_list_item_1, cname);
                                select.setAdapter( adpt );
                            }

                            // }
                            else {
                                Toast.makeText(getApplicationContext(), "Not found", Toast.LENGTH_LONG).show();
                            }

                        }    catch (Exception e) {
                            Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // error
                        Toast.makeText(getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                    }
                }
        ) {
            @Override
            protected Map<String, String> getParams() {
                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                Map<String, String> params = new HashMap<String, String>();

                String id=sh.getString("logid","");
                params.put("uid",id);
//                params.put("mac",maclis);

                return params;
            }
        };

        int MY_SOCKET_TIMEOUT_MS=100000;

        postRequest.setRetryPolicy(new DefaultRetryPolicy(
                MY_SOCKET_TIMEOUT_MS,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
        requestQueue.add(postRequest);
    }

    @Override
    public void onClick(View view) {
        float rating=r1.getRating();
        final String rr=Float.toString( rating );
        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences( getApplicationContext() );
        String hu = sh.getString( "ip", "" );
        String url = "http://" + hu + ":5000/and_insertcouncillor";


        RequestQueue requestQueue = Volley.newRequestQueue( getApplicationContext() );
        StringRequest postRequest = new StringRequest( Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        Toast.makeText( getApplicationContext(), response, Toast.LENGTH_LONG ).show();

                        // response
                        try {
                            JSONObject jsonObj = new JSONObject( response );
                            if (jsonObj.getString( "status" ).equalsIgnoreCase( "Inserted" )) {

                                startActivity( new Intent( getApplicationContext(), Councillorrating.class ) );

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
                params.put( "rating", rr );
                params.put("did",did1);

                return params;
            }
        };

        int MY_SOCKET_TIMEOUT_MS = 100000;

        postRequest.setRetryPolicy( new DefaultRetryPolicy(
                MY_SOCKET_TIMEOUT_MS,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT ) );
        requestQueue.add( postRequest );


    }

    @Override
    public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
        did1=did[i];

    }

    @Override
    public void onNothingSelected(AdapterView<?> adapterView) {

    }
}
