from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.viewTask, name='home'),
    path('tasks/<int:pk>/', views.updateTask, name='update_task'),
    path('tasks/<int:pk>/delete', views.deleteTask, name='delete_task'),
]
