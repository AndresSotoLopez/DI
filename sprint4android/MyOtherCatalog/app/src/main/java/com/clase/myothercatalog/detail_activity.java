package com.clase.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.content.Intent;
import android.media.Image;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

public class detail_activity extends AppCompatActivity {
    
    //Definicion de las variables
    public static final String TITLE = "TITLE" ;
    public static final String URL = "URL" ;
    public static final String DESCRIPTION = "DESCRIPTION" ;
    private String url;
    private String description;
    private String title;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);
    
        ImageView image = findViewById(R.id.imageview_detail_activity);
        TextView title_detail = findViewById(R.id.textview_detail_activity);
        TextView description_detail = findViewById(R.id.description_detail_activity);
    
    
        Intent intent = getIntent();
        
        title = intent.getStringExtra(TITLE);
        description = intent.getStringExtra(DESCRIPTION);
        url = intent.getStringExtra(URL);
        
        Glide.with(detail_activity.this).load(url).into(image);
        title_detail.setText(title);
        description_detail.setText(description);
        
    }
}