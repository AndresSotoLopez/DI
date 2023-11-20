package com.clase.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class cod_data {
    
    private final String title;
    private final String description;
    private final String url;
    
    public cod_data(JSONObject data) throws JSONException {
        
        this.title = data.getString("name");
        this.description = data.getString("description");
        this.url = data.getString("img_url");
        
    }
    
    //------------------------------------------------------------------------GET------------------------------------------------------------------------
    public String getTitle() {
        return title;
    }
    
    public String getDescription() {
        return description;
    }
    
    public String getUrl() {
        return url;
    }
}
