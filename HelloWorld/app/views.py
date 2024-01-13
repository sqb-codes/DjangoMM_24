from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "Ravikant Tyagi"
    return render(request, "index.html", context={"name":name})

def login(request):
    return HttpResponse("Login Success...")