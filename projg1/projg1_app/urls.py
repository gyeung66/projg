from django.urls import path
from .views import hello,revcomp, start

urlpatterns = [
    path("", hello, name="hello"),
    path("start/", start, name="start"),
    path("revcomp", revcomp, name="revcomp"),
    ]