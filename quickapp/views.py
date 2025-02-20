from django.shortcuts import render

# Create your views here.
def index(request):
    return  render(request, 'home.html')

def gallery(request):
    return render(request, 'Gallery.html')

def about(request):
    return render(request, 'about.html')

def form(request):
    return render(request, 'form.html')

def products(request):
    return render(request, 'products.html')

def services(request):
    return render(request, 'services.html')
