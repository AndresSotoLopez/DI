package com.clase.myothercatalog;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

import java.util.List;

public class adapter extends RecyclerView.Adapter<adapter.MyViewHolder> {
    
    //Definicion de las variables
    private final List<cod_data> cod_list;
    private final LayoutInflater layoutInflater;
    private final Context context;
    
    //Constructor
    public adapter(List<cod_data> cod_list, Context context) {
        this.layoutInflater = LayoutInflater.from(context);
        this.cod_list = cod_list;
        this.context = context;
    }
    
    //Funcion que nos permite crear la vista de nuestra recyclerview
    @NonNull
    @Override
    public adapter.MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = layoutInflater.inflate(R.layout.element, null);
        return new MyViewHolder(view);
    }
    
    //Funcion que nos permite actualizar la vista de nuestro recyclerview
    @Override
    public void onBindViewHolder(@NonNull adapter.MyViewHolder holder, int position) {
        
        cod_data cod_data = cod_list.get(position);
        
        holder.title.setText(cod_data.getTitle());
        Glide.with(context).load(cod_data.getUrl()).into(holder.image);
        
    }
    
    // Funcion que nos permite obtener el tamaño de la lista
    @Override
    public int getItemCount() {
        return cod_list.size();
    }
    
    //Clase que nos permite obtener la vista de nuestra recyclerview
    public static class MyViewHolder extends RecyclerView.ViewHolder{
        
         ImageView image;
         TextView title;
        
        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            
            image = itemView.findViewById(R.id.iconImageView);
            title = itemView.findViewById(R.id.cod_title);
            
        }
        
    }
}
