from django.shortcuts import render
from django.http import JsonResponse
import json

contant_data = {"message": "This is xxx"}
# Create your views here.
def hello(request):
    """
    A simple view that returns a greeting.
    """
    context = {
        'greeting': 'Hello, World!'
    }
    return render(request, 'hello.html', context)

def home(request):
    """
    A simple home view that returns a welcome message.
    """
    context = {
        'message': 'Welcome to the Home Page!'
    }
    return render(request, 'index.html', context)

def newpage(request):
    """
    A new page view that returns a message.
    """
    context = {
        'message': 'This is a neww page!'
    }
    return render(request, 'newpage.html', context)

def rec_data(request):  
    if request.method == 'POST':
        data = json.loads(request.body)
        print("received data:", data["data"]) 
        print(type(request))
        contant_data["data"] = data["data"][1]  # Update the message with received data
        print("contant_data:", contant_data)
        context = {
            'message': 'Received data'
        }
    #return render(request, 'rec_data.html', context)
    return JsonResponse({"message": "success"})

print("a, b,c")
