from django.shortcuts import render
from django.http import HttpResponse 
from .models import Student 


# Create your views here.

def Home(request):
    
    info = {
        'name' : "Ajay" , 
        'age' : 20 , 
    }
    return render(request, 'home/index.html')




