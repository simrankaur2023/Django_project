from app1 import views as main_view
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    # path('', main_view.Index),
    path('', main_view.home),
    path('monday/', main_view.menu),
    path('contact/', main_view.contact),
    path('about/', main_view.about),
    path('work/<days>/' , main_view.work)
    ]
