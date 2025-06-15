from django.urls import path
from .views import input, result

urlpatterns = [
    path('', input, name='input'),  # URL for the input page
    path('result', result, name='result'),  # URL for the result page
]