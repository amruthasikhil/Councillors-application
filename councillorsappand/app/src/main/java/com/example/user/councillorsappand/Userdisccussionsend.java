package com.example.user.councillorsappand;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
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

public class Userdisccussionsend extends AppCompatActivity implements View.OnClickListener {
    Button b1;
    ListView li;
    String[] comment,name,image;
    EditText e1;
    String commnt;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );
        setContentView( R.layout.activity_userdisccussionsend );
        e1=(EditText)findViewById( R.id.editText2 );
        b1=(Button) findViewById( R.id.button3 );
        b1.setOnClickListener( this );
        li=(ListView)findViewById( R.id.list8 );
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        String hu = sh.getString("ip", "");
        String url = "http://" + hu + ":5000/and_discussionview";



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
                                 comment=new String[js.length()];
                                image=new String[js.length()];
                                name=new String[js.length()];

//
                                for(int i=0;i<js.length();i++)
                                {
                                    JSONObject u=js.getJSONObject(i);
                                    comment[i]=u.getString("comment");//dbcolumn name
                                    image[i]=u.getString("image");
                                    name[i]=u.getString("name");


                                }
//                                for(int i=0;i<js1.length();i++)
//                                {
//                                    JSONObject u=js1.getJSONObject(i);
//
//                         rating[i]=u.getString("rating");
//
//                                }

                                // ArrayAdapter<String> adpt=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,name);
//                                gv.setAdapter(new Custom_view_visited_game(getApplicationContext(),name,gamecode));
                                li.setAdapter(new custom_userdiscussionsend(getApplicationContext(),image,comment,name));//custom_view_service.xml and li is the listview object
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
                String dis=sh.getString("disid","");
                params.put("uid",id);
                params.put("did",dis);

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
        if(view==b1){
            int flag=0;
       commnt=e1.getText().toString();
            if(commnt.equalsIgnoreCase(""))
            {
                e1.setError("*");
                flag++;
            }
            if(flag==0)
            {

        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences( getApplicationContext() );

        String hu = sh.getString( "ip", "" );
        String url = "http://" + hu + ":5000/and_discussioninsert";


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

                                startActivity( new Intent( getApplicationContext(), Userdisscussionview.class ) );

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

                String id=sh.getString("logid","");
                String dis=sh.getString("disid","");
                params.put("uid",id);
                params.put("did",dis);
                params.put("comment",commnt);
                return params;
            }
        };

        int MY_SOCKET_TIMEOUT_MS = 100000;

        postRequest.setRetryPolicy( new DefaultRetryPolicy(
                MY_SOCKET_TIMEOUT_MS,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT ) );
        requestQueue.add( postRequest );

    }}}
}
