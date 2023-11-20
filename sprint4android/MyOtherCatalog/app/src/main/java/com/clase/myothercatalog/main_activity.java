package com.clase.myothercatalog;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
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
    
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_layout);
        
        RecyclerView recyclerView = (RecyclerView) findViewById(R.id.list_recycler_view);
        //Definicion de variables
        List<cod_data> cod_list = peticion();
        
        
    }
    
    //Funcion que nos lanzará la peticion get a nuestro github : "https://raw.githubusercontent.com/AndresSotoLopez/DI/main/recursos/catalog.json"
   
    private List<cod_data> peticion(){
        
        List<cod_data> cod_list = new ArrayList<>();
        
        JsonArrayRequest request = new JsonArrayRequest
            (Request.Method.GET,
            "https://raw.githubusercontent.com/AndresSotoLopez/DI/main/recursos/catalog.json", 
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

            RequestQueue requestQueue = Volley.newRequestQueue(this);
            requestQueue.add(request);
        
            return cod_list;
    }
    
}