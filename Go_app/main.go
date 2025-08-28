package main

import (
    "fmt"
    "net/http"
    "github.com/gorilla/mux"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello from Go app with dependencies!")
}

func main() {
    r := mux.NewRouter()
    r.HandleFunc("/", handler)
    fmt.Println("Server running on port 8080")
    http.ListenAndServe(":8080", r)
}
