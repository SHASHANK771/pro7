from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')    

	
# Create your views here.
def h1(request):
    return render(request,'h1.html')    