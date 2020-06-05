

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('panel/news/addcat',views.add_cat,name="addcat"),
   path('panel/news/managecat',views.manage_cat,name="managecat"),


]
