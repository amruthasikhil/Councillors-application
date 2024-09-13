package com.example.user.councillorsappand;

import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.squareup.picasso.Picasso;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class Userprojectmore extends AppCompatActivity {
    TextView t1,t2,t3,t4,t5;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );
        setContentView( R.layout.activity_userprojectmore );
        t1=(TextView)findViewById( R.id.textView32 );
        t2=(TextView)findViewById( R.id.textView34 );
        t3=(TextView)findViewById( R.id.textView36 );
        t4=(TextView)findViewById( R.id.textView40 );
        t5=(TextView)findViewById( R.id.textView43 );

        SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences( getApplicationContext() );

        String hu = sh.getString("ip", "");
        String url = "http://" + hu + ":5000/and_userprojectviewmore";



        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        StringRequest postRequest = new StringRequest( Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();

                        // response
                        try {
                            JSONObject jsonObj = new JSONObject(response);

                            if (jsonObj.getString("status").equalsIgnoreCase("ok")) {

                                JSONObject jj= jsonObj.getJSONObject("data");
                                String na=jj.getString("name");
                                t1.setText(na);
                                String details=jj.getString("details");
                                t2.setText(details);
                                String date=jj.getString("date");
                                t3.setText(date);
                                String enddate=jj.getString("enddate");
                                t5.setText(enddate);

                                String amount=jj.getString("amount");
                                t4.setText( amount );
                            }



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
                SharedPreferences sh1 = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                Map<String, String> params = new HashMap<String, String>();

                String id=sh1.getString("proid","");
//                String reqid=sh.getString("reqid","");
                params.put("pid",id);
//                params.put("reqid",reqid);
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
}
