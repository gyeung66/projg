from django.shortcuts import render
import json

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
    """
    A view that processes data from a form submission.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        print("received data:", data["data"][1])  # Debugging line to check received data
        context = {
            'message': 'Received data'
        }
        return render(request, 'rec_data.html', context)
    else:
        return render(request, 'rec_data.html', {'message': 'No d-ata received.'})