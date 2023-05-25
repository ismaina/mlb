from django.urls import path
from .views import (index, contact, about)

app_name ='frontend'
urlpatterns = [
    path("",index, name='index' ),
    path("contact/",contact, name='contact' ),
    path("about/",about, name='about' ),
    
]
