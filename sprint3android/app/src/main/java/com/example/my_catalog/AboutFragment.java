package com.example.my_catalog;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

public class AboutFragment extends Fragment {
    public static AboutFragment newInstance() {
        return new AboutFragment(); //Creamos el nuevo fragmento para devolverlo cuando pulsemos sobre la opcion.
    }
    
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable
    Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_about, container, false); //Devolvemos una view, ya inflada donde veremos el contenido del fragmento.
    }
}