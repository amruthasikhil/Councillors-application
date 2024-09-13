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

public class Coodinatorcounview extends AppCompatActivity {
    TextView t1,t2,t3,t4,t5,t6,t7,t8,t9,t10;
    ImageView i2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );
        setContentView( R.layout.activity_coodinatorcounview );
        t1=(TextView)findViewById( R.id.textView54 );
        t2=(TextView)findViewById( R.id.textView60 );
        t3=(TextView)findViewById( R.id.textView61 );
        t4=(TextView)findViewById( R.id.textView63 );
        t5=(TextView)findViewById( R.id.textView65 );
        t6=(TextView)findViewById( R.id.textView67 );
        t8=(TextView)findViewById( R.id.textView71 );
        t9=(TextView)findViewById( R.id.textView75 );
        t10=(TextView)findViewById( R.id.textView77 );
        i2=(ImageView)findViewById( R.id.imageView9 );
        SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences( getApplicationContext());

        String hu = sh.getString("ip", "");
        String url = "http://" + hu + ":5000/and_coordinatorcouncillor";



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
                                String gender=jj.getString("gender");
                                t2.setText(gender);
                                String dob=jj.getString("dob");
                                t3.setText(dob);
                                String hn=jj.getString("house_name");
                                t4.setText(hn);
                                String place=jj.getString("place");
                                t5.setText(place);
                                String pin=jj.getString("pincode");
                                t6.setText(pin);
                                String email=jj.getString("email");
                                t8.setText(email);
                                String ph=jj.getString("phone");
                                t9.setText(ph);
                                String ward=jj.getString("ward");
                                t10.setText(ward);

                                String image=jj.getString("image");
                                SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                                String ip=sh.getString("ip","");
                                String url="http://" + ip + ":5000"+image;
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
                params.put("uid",id);
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
