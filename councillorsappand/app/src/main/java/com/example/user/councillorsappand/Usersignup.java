package com.example.user.councillorsappand;

import android.Manifest;
import android.app.ProgressDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Build;
import android.preference.PreferenceManager;
import android.provider.MediaStore;
import android.provider.Settings;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Usersignup extends AppCompatActivity implements View.OnClickListener {
    EditText e1,e2,e3,e4,e5,e6,e7,e8,e9;
    Button b1;
    ImageView i;
    String name,phone,password,cpass,email,place,pin,ward,post;
    Bitmap bitmap=null;
    ProgressDialog pd;
    SharedPreferences sh;
    String apiURL="";
    long imagename=0;
    int flag=0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );
        setContentView( R.layout.activity_usersignup );
        e1=(EditText)findViewById(R.id.txt_name );
        e2=(EditText)findViewById(R.id.txt_place);
        e3=(EditText)findViewById(R.id.txt_post);
        e4=(EditText)findViewById(R.id.txt_pin);
        e5=(EditText)findViewById(R.id.txt_email);
        e6=(EditText)findViewById(R.id.txt_phone);
        e7=(EditText)findViewById(R.id.txt_ward);
        e8=(EditText)findViewById(R.id.txt_pass);
        e9=(EditText)findViewById(R.id.txt_cpass);
        i=(ImageView)findViewById( R.id.imageView );
        b1=(Button)findViewById( R.id.btn);
        b1.setOnClickListener( this );


        sh= PreferenceManager.getDefaultSharedPreferences(Usersignup.this);
        apiURL="http://" + sh.getString("ip","") + ":5000/user_registration";

//        Checking set permission

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && ContextCompat.checkSelfPermission(this,
                Manifest.permission.READ_EXTERNAL_STORAGE)
                != PackageManager.PERMISSION_GRANTED) {
            Intent intent = new Intent( Settings.ACTION_APPLICATION_DETAILS_SETTINGS,
                    Uri.parse("package:" + getPackageName()));
            finish();
            startActivity(intent);
            return;
        }
        //Opening gallery
        i.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
                startActivityForResult(i, 100);
            }
        });

    }

    @Override
    public void onClick(View view) {
        if (view==b1)
        {
            name=e1.getText().toString();
            place=e2.getText().toString();
            post=e3.getText().toString();
            pin=e4.getText().toString();
            email=e5.getText().toString();
            phone=e6.getText().toString();
            ward=e7.getText().toString();
            password=e8.getText().toString();
            cpass=e9.getText().toString();

            if(name.equalsIgnoreCase(""))
            {
                e1.setError("*");
                flag++;
            }
            if(place.equalsIgnoreCase(""))
            {
                e2.setError("*");
                flag++;
            }
            if(post.equalsIgnoreCase(""))
            {
                e3.setError("*");
                flag++;
            }
            if(pin.equalsIgnoreCase(""))
            {
                e4.setError("*");
                flag++;
            }
            if(email.equalsIgnoreCase(""))
            {
                e5.setError("*");
                flag++;
            }
            if(phone.equalsIgnoreCase(""))
            {
                e6.setError("*");
                flag++;
            }
            if(ward.equalsIgnoreCase(""))
            {
                e7.setError("*");
                flag++;
            }
            if(password.equalsIgnoreCase(""))
            {
                e8.setError("*");
                flag++;
            }
            if(cpass.equalsIgnoreCase(""))
            {
                e9.setError("*");
                flag++;
            }
            if(imagename==0)
            {
                Toast.makeText( this, "Choose pic..", Toast.LENGTH_SHORT ).show();
            }
            if(!android.util.Patterns.EMAIL_ADDRESS.matcher(email).matches())
            {
                e5.setError("Invalid email");
                flag++;
            }
            if(phone.length()!=10)
            {
                e6.setError("Invalid Format");
                flag++;
            }
            if (flag==0)
            {
                uploadBitmap();
                Intent in=new Intent( getApplicationContext(),Usersignup.class );
                startActivity( in );
            }


        }
    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == 100 && resultCode == RESULT_OK && data != null) {

            Uri imageUri = data.getData();
            try {
                bitmap = MediaStore.Images.Media.getBitmap(this.getContentResolver(), imageUri);

                i.setImageBitmap(bitmap);//set bitmap to imageview


            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public byte[] getFileDataFromDrawable(Bitmap bitmap) {
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        bitmap.compress(Bitmap.CompressFormat.PNG, 80, byteArrayOutputStream);
        return byteArrayOutputStream.toByteArray();
    }

    private void uploadBitmap() {

        pd=new ProgressDialog(Usersignup.this);
        pd.setMessage("Uploading....");
        pd.show();
        VolleyMultipartRequest volleyMultipartRequest = new VolleyMultipartRequest( Request.Method.POST, apiURL,
                new Response.Listener<NetworkResponse>() {
                    @Override
                    public void onResponse(NetworkResponse response) {
                        try {
                            pd.dismiss();
                            JSONObject obj = new JSONObject(new String(response.data));
                            Toast.makeText(getApplicationContext(), obj.getString("message"), Toast.LENGTH_SHORT).show();
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(getApplicationContext(), error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }) {


            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                Map<String, String> params = new HashMap<>();
                params.put("name", name);
                params.put("email", email);
                params.put("phone", phone);
                params.put("place", place);
                params.put("pin", pin);
                params.put("post", post);
                params.put("ward", ward);
                params.put("password", password);
                params.put("cpass", cpass);
                return params;
            }


            @Override
            protected Map<String, DataPart> getByteData() {
                Map<String, DataPart> params = new HashMap<>();
                 imagename = System.currentTimeMillis();
                params.put("pic", new DataPart(imagename + ".png", getFileDataFromDrawable(bitmap)));
                return params;
            }
        };

        Volley.newRequestQueue(this).add(volleyMultipartRequest);
    }

}


