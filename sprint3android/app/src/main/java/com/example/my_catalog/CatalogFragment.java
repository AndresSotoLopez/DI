package com.example.my_catalog;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

public class CatalogFragment extends Fragment {
    //Variables
    private Context context;
    public static CatalogFragment newInstance() {
        //Retornamos directamente la nueva instancia del fragmento
        return new CatalogFragment();
    }
    
    
    @Override
    public void onAttach(Context new_context) {
        //Juntamos el fragmento con la actividad a la que pertenece
        super.onAttach(new_context);
        this.context = new_context;
    }
    
    
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
    
        //Creacion de la variable layout y la variable Button
        View layout = inflater.inflate(R.layout.fragment_catalog, container, false);
        Button button = layout.findViewById(R.id.catalog_fragment_button);
        
        //Funcion encargada de lanzar la nueva actividad si se llega a pulsar el boton
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (context != null) {
                    Intent myIntent = new Intent(context, DetailActivity.class);
                    context.startActivity(myIntent);
                }
            }
        });
        return layout;
    }
}