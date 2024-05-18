from django.contrib import admin
from django.urls import path, include

from blog.views import home, category, akshin
urlpatterns = [
    path('', home, name='home'),
    path('anasehife/', akshin, name='akshin'),
    path('category/<slug:slug>/', category, name='category'),
]