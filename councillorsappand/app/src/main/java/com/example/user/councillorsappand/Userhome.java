package com.example.user.councillorsappand;

import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;
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

public class Userhome extends AppCompatActivity {
    TextView t1,t2,t3;
    ImageView i2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );
        setContentView( R.layout.activity_userhome );
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        t1=(TextView)findViewById(R.id.textView38);
        t2=(TextView)findViewById(R.id.textView39);
        t3=(TextView)findViewById(R.id.textView41);
//        tb2=(TabLayout) findViewById(R.id.adv);
        i2=(ImageView)findViewById(R.id.imageView3);
//        tb2.addOnTabSelectedListener(this);


        String hu = sh.getString("ip", "");
        String url = "http://" + hu + ":5000/uprofile";



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
                                String email=jj.getString("email");
                                t2.setText(email);
                                String phone=jj.getString("phone");
                                t3.setText(phone);

                                String image1=jj.getString("image");
                                SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                                String ip=sh.getString("ip","");
                                String url="http://" + ip + ":5000"+image1;
                                Picasso.with(getApplicationContext()).load(url).transform(new CircleTransform()). into(i2);//circle

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
                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                Map<String, String> params = new HashMap<String, String>();

                String id=sh.getString("logid","");
//                String reqid=sh.getString("reqid","");
                params.put("uid",id);
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

