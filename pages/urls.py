from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('landing',views.landing,name='landing'),
    path('insert',views.insert,name='insert'),
    path('deleteintake/<id>',views.deleteintake,name='deleteintake'),
    path('updateintake/<id>',views.updateintake,name='updateintake')
]