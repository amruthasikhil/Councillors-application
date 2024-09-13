package com.example.user.councillorsappand;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
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

public class Umayorview extends AppCompatActivity implements View.OnClickListener {
    TextView t1,t2,t3,t4,t5,t6,t7,t8,t9,t10;
    ImageView i2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );
        setContentView( R.layout.activity_umayorview );
        t1=(TextView)findViewById(R.id.textView38e);
        t2=(TextView)findViewById(R.id.cplace);
        t3=(TextView)findViewById(R.id.textView7);
        t4=(TextView)findViewById(R.id.cpin);
        t5=(TextView)findViewById(R.id.cphone);
        t6=(TextView)findViewById(R.id.cemail);
        t7=(TextView)findViewById(R.id.cperiod);
        t8=(TextView)findViewById(R.id.dob);
        t9=(TextView)findViewById(R.id.textView38);
        t10=(TextView)findViewById(R.id.textView9);
        i2=(ImageView)findViewById(R.id.imageView2);
        t10.setOnClickListener(this);
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String hu = sh.getString("ip", "");
        String url = "http://" + hu + ":5000/and_mayorview";
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
                                String na=jj.getString("mayor_name");
                                t1.setText(na);
                                String place=jj.getString("place");
                                t2.setText(place);
                                String post=jj.getString("enddate");
                                t3.setText(post);
                                String pin=jj.getString("pincode");
                                t4.setText(pin);
                                String email=jj.getString("email");
                                t6.setText(email);
                                String phone=jj.getString("phone");
                                t5.setText(phone);
                                String period=jj.getString("joindate");
                                t7.setText(period);
                                String dob=jj.getString("dob");
                                t8.setText(dob);
                                String hname=jj.getString("house_name");
                                t9.setText(hname);

                                String image1=jj.getString("picture");
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

    @Override
    public void onClick(View view) {
        if(view==t10){
            Intent in=new Intent( getApplicationContext(),Usermayorview.class );
            startActivity( in );
        }

    }
}
