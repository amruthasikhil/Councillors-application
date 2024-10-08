package com.example.user.councillorsappand;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;

public class Coordinatorhomepages extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate( savedInstanceState );
        setContentView( R.layout.activity_coordinatorhomepages );
        Toolbar toolbar = (Toolbar) findViewById( R.id.toolbar );
        setSupportActionBar( toolbar );

        FloatingActionButton fab = (FloatingActionButton) findViewById( R.id.fab );
        fab.setOnClickListener( new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make( view, "Replace with your own action", Snackbar.LENGTH_LONG )
                        .setAction( "Action", null ).show();
            }
        } );

        DrawerLayout drawer = (DrawerLayout) findViewById( R.id.drawer_layout );
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close );
        drawer.addDrawerListener( toggle );
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById( R.id.nav_view );
        navigationView.setNavigationItemSelectedListener( this );
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById( R.id.drawer_layout );
        if (drawer.isDrawerOpen( GravityCompat.START )) {
            drawer.closeDrawer( GravityCompat.START );
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate( R.menu.coordinatorhomepages, menu );
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected( item );
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_profile) {
            Intent ij=new Intent( getApplicationContext(),Coorperationhome.class);
            startActivity( ij );
        } else if (id == R.id.nav_viewcouncillor) {
            Intent ij=new Intent( getApplicationContext(),Coodinatorcounview.class);
            startActivity( ij );

        } else if (id == R.id.nav_viewservice) {
            Intent ij=new Intent( getApplicationContext(),Userviewservice.class);
            startActivity( ij );

        } else if (id == R.id.nav_viewpolicy) {
            Intent ij=new Intent( getApplicationContext(),Coordinatorpolicyview.class);
            startActivity( ij );

        } else if (id == R.id.nav_publicneedreporting) {
            Intent ij=new Intent( getApplicationContext(),Coorperationhome.class);
            startActivity( ij );

        }
        else if (id == R.id.nav_viewallocatedfund) {
            Intent ij=new Intent( getApplicationContext(),Fundallocationtocoordinator.class);
            startActivity( ij );

        }
        else if (id == R.id.nav_viewnotification1) {
            startActivity(new Intent(getApplicationContext(),Usernotification.class));

        }
        else if (id == R.id.nav_chatwithcouncilllor) {
            startActivity(new Intent(getApplicationContext(),Chatwithcouncillor.class));

        }
        else if (id == R.id.nav_projectview) {
            startActivity(new Intent(getApplicationContext(),Userprojectview.class));

        }
        else if (id == R.id.nav_logout1) {
            startActivity(new Intent(getApplicationContext(),Logout.class));

        }


        DrawerLayout drawer = (DrawerLayout) findViewById( R.id.drawer_layout );
        drawer.closeDrawer( GravityCompat.START );
        return true;
    }
}
