from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('insert/', views.insert, name = "insert"),
    path('insertData/', views.insertData, name = "insertData"),
    path('viewdata/', views.viewtable, name = "viewdata"),
    path('edit/<id>', views.edit, name="edit"),
]