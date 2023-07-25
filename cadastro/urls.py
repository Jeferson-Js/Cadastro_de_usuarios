from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create_user/', views.create_user, name="create_user"),
    path('edit_user/<int:id>', views.edit_user, name="edit_user"),
    path('delete_user/<int:id>', views.delete_user, name="delete_user")
]