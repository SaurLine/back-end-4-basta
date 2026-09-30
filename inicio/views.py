from django.shortcuts import render

# Create your views here.
def default(request):
    productos = [
        {"codigo":1,"nombre":"Producto","descripcion":"Producto 1","stock":"1","precio":"$1.000"},
        {"codigo":2,"nombre":"Producto","descripcion":"Producto 2","stock":"2","precio":"$1.000"},
        {"codigo":3,"nombre":"Producto","descripcion":"Producto 3","stock":"3","precio":"$1.000"},
        {"codigo":4,"nombre":"Producto","descripcion":"Producto 4","stock":"4","precio":"$1.000"},
        {"codigo":5,"nombre":"Producto","descripcion":"Producto 5","stock":"5","precio":"$1.000"}
    ]
    return render(request, "inicio/default.html",{"articulos":productos})