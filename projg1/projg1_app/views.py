from django.shortcuts import render

# Create your views here.
def hello(request):
    """
    A simple view that returns a greeting.
    """
    return render(request, 'hello.html', {'greeting': 'Hello, World!'})

