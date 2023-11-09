package com.example.my_catalog;

import androidx.annotation.NonNull;
import androidx.annotation.StringRes;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import android.os.Bundle;
import android.view.MenuItem;

import com.google.android.material.navigation.NavigationView;

public class CatalogActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener {
    
    //Declaracion de Variables
    private DrawerLayout drawerLayout;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.nav_view);
        
        //Implementacion de la nueva toolbar
        Toolbar toolbar = (Toolbar) findViewById(R.id.activity_catalog_toolbar);
        setSupportActionBar(toolbar);
        
        //Configuracion del DrawerLayout
        drawerLayout = findViewById(R.id.drawer_layout);
        NavigationView navigationView = findViewById(R.id.navigation_view);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        
        //Añadimos al drawerLayout el toggle creado arriba
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();
        //Instanciamos al navigationView una lista de seleccion
        navigationView.setNavigationItemSelectedListener(this);
    }
    
    @Override
    public void onBackPressed() {
        //Cerramos el Drawer en caso de que este abierto
        if (drawerLayout.isDrawerOpen(GravityCompat.START))
            drawerLayout.closeDrawer(GravityCompat.START);
        else
            super.onBackPressed();
    }
    
    //Una vez seleccionado el fragment que queremos ver pulsando en el, el drawer se cerrara
    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
        // Obtiene la ID del título seleccionado del menú
        int titleId = getTitle(menuItem);
        showFragment(titleId);
        //Cerramos el drawer al cambiar de fragment
        drawerLayout.closeDrawer(GravityCompat.START);
        return true;
    }
    
    private int getTitle(@NonNull MenuItem menuItem) {
        String itemId = (String) menuItem.getTitle();
        
        //En caso, como solo tenemos 2 fragments,en el caso de que el itemId sea Home devolvemos su stringCorrespondiente, si no, devolvemos el string correspondiente al About
        if (itemId.equals("Home"))
            return R.string.CatalogFragment;
         
        return R.string.AboutFragment;
    }
    
    private void showFragment(@StringRes int titleId) {
        if (titleId == R.string.CatalogFragment) {
            //En caso de eque el titulo obtenido sea, el titulo de Catalog, se creara una nueva instancia del fragmento
            getSupportFragmentManager().beginTransaction().replace(R.id.home_content, CatalogFragment.newInstance()).commit();
            setTitle(getString(titleId));
            return;
        }
        //En caso contrario siempre muestra el About Fragment
        getSupportFragmentManager().beginTransaction().replace(R.id.home_content, AboutFragment.newInstance()).commit();
        setTitle(getString(titleId));
        
    }
}