from django.shortcuts import render
import json

# Create your views here.
def home(request):
    """
    Render the home page.
    """
    return render(request, 'home.html')
def newpage(request):
    """
    Render the new page.
    """
    return render(request, 'newpage.html')
def rec_data(request):
    """
    Handle data submission and render the response.
    """
    if request.method == 'POST':
        data = request.POST["hot_data"]
        rec_data = json.loads(data)
        print(type(rec_data[0][0]))
        print(int(rec_data[0][0]) + 10)
        return render(request, 'rec_data.html', {'data': data, 'message': 'Data received successfully'})
    else:
        return render(request, 'rec_data.html', {'data': 'no data submitted'})