from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def login(req):
    return render(req, 'login.html')

def register(req):
    return render(req, 'register.html')

def registerUser(req):
    username = req.POST['name']
    email = req.POST['email']
    password = req.POST['pwd']

    return render(req, 'index.html', {'username':username})