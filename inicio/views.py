from django.shortcuts import render

# Create your views here.
def default(request):
    return render(request, "inicio/default.html")