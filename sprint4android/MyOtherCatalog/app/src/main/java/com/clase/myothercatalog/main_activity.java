package com.clase.myothercatalog;

import android.content.Context;
import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class main_activity extends AppCompatActivity {
   
    //Definicion de las variables
    private RecyclerView recyclerView;
    
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_layout);
        
        recyclerView = (RecyclerView) findViewById(R.id.recyclerview);
        peticion();
    }
    
    //Funcion que nos lanzará la peticion get a nuestro github : "https://raw.githubusercontent.com/AndresSotoLopez/DI/main/recursos/catalog.json"
   
    private void peticion(){
        
        //Creacion de la lista para guardar los datos de la peticion
        List<cod_data> cod_list = new ArrayList<>();
        
        //Creamos una peticion para obtener los datos del JSON
        JsonArrayRequest request = new JsonArrayRequest
            (Request.Method.GET,
            "https://raw.githubusercontent.com/AndresSotoLopez/DI/main/recursos/more_catalog.json",
            null, 
            new Response.Listener<JSONArray>(){
                @Override
                public void onResponse(JSONArray response) {
                    try {

                        //Recorremos el array de datos de la peticion
                        for(int i = 0; i < response.length(); i++){
                            JSONObject jsonObject = response.getJSONObject(i);
                            cod_data cod_data = new cod_data(jsonObject);
                            cod_list.add(cod_data);
                        }
                        
                        //Mostramos el recyclerview a traves de nuestro adapter
                        adapter adapter = new adapter(cod_list, main_activity.this);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(main_activity.this));
                        
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                    
                }
            },
                new Response.ErrorListener() {
    
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        error.printStackTrace();
                    }
                }
            );
        
        Volley.newRequestQueue(this).add(request);
    }
    
    
}