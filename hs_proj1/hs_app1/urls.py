from django.urls import path
from .views import hello, home, newpage, rec_data
urlpatterns = [
    path('', hello, name='hello'),
    path('home/', home, name='home'),
    path('newpage', newpage, name='newpage'),
    path('rec_data', rec_data, name='rec_data'),
]