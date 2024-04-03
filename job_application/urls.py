from django.urls import path
from . import views


# these are the urls that we are managing
# about.html -> website.com/about/

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')
]

# index is coming from the views file
