

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('panel/news/addsubcat',views.add_subcat,name="addsubcat"),
   path('panel/news/managesubcat',views.manage_subcat,name="managesubcat"),


]
