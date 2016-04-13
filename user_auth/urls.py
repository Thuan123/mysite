from django.conf.urls import url
 
from . import views

app_name = "user_auth"
urlpatterns = [
    url(r'^$', views.register),
]