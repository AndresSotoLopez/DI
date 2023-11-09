package com.example.my_catalog;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //Mostramos el layout de la actividad
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);
    }
}