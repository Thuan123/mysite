from django.conf.urls import url 
 
from . import views
from views import *
from django.conf import settings
from django.conf.urls.static import static 

app_name = "polls" 
urlpatterns = [
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/signup
    url(r'^login', views.signup, name='signup'),
    # ex: /polls/login
    url(r'^login', views.LoginView.as_view(), name='login'),
    # ex: /polls/5/
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
