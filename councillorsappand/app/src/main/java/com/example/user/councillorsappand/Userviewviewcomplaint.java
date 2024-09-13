package com.example.user.councillorsappand;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.design.widget.FloatingActionButton;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
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

public class Userviewviewcomplaint extends AppCompatActivity implements View.OnClickListener {
    ListView li;
    String[] complaint,date,rply,todate;
    FloatingActionButton fab;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );
        setContentView( R.layout.activity_userviewviewcomplaint );
        li=(ListView)findViewById( R.id.list5 );
//
        fab = (FloatingActionButton) findViewById( R.id.fab1 );
        fab.setOnClickListener( this );
////        fab.setOnClickListener( new View.OnClickListener() {
////            @Override
////            public void onClick(View view) {
////                Snackbar.make( view, "Replace with your own action", Snackbar.LENGTH_LONG )
////                        .setAction( "Action", null ).show();
////                Intent ij=new Intent( getApplicationContext(),Usersendnotification.class );
////                startActivity( ij );
////            }
////        } );
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences( getApplicationContext() );

        String hu = sh.getString("ip", "");
        String url = "http://" + hu + ":5000/and_addcomplaints";

        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        StringRequest postRequest = new StringRequest( Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
//                        Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();


                        // response
                        try {
                            JSONObject jsonObj = new JSONObject(response);
                            if (jsonObj.getString("status").equalsIgnoreCase("ok")) {
//view service code
                                JSONArray js= jsonObj.getJSONArray("data");//from python
                                complaint=new String[js.length()];
                                date=new String[js.length()];
                                rply=new String[js.length()];
                                todate=new String[js.length()];
//
                                for(int i=0;i<js.length();i++)
                                {
                                    JSONObject u=js.getJSONObject(i);
                                    complaint[i]=u.getString("complaint");//dbcolumn name
                                    date[i]=u.getString("complaint_date");
                                    rply[i]=u.getString("reply");
                                    todate[i]=u.getString("reply_date");
//                                    Toast.makeText(getApplicationContext(), Photo.toString(), Toast.LENGTH_LONG).show();
//
                                }
//

//                                 ArrayAdapter<String> adpt=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,complaint);
//                              li.setAdapter( adpt );
                                li.setAdapter(new custom_userviewcomplaint(getApplicationContext(),complaint,date,rply,todate));//custom_view_service.xml and li is the listview object

//
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
        Intent ij=new Intent( getApplicationContext(),Usersendnotification.class );
                startActivity( ij );

    }
}
