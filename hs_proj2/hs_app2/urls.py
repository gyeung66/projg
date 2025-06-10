from django.urls import path
from .views import home, newpage, rec_data
urlpatterns = [
    path('', home, name='home'),
    path('newpage', newpage, name='newpage'),
    path('rec_data', rec_data, name='rec_data'),
]