package com.example;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

public class App {
    public static void main(String[] args) {
        String jsonString = "{\"name\": \"Mahmoud Sallam\", \"role\": \"DevOps Engineer\", \"os\": \"Linux\"}";

        JsonObject obj = JsonParser.parseString(jsonString).getAsJsonObject();
        System.out.println("Name: " + obj.get("name").getAsString());
        System.out.println("Role: " + obj.get("role").getAsString());
        System.out.println("Operating System: " + obj.get("os").getAsString());
    }
}
