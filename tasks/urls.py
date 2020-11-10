from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks', views.tasks, name='tasks'),
    path('create', views.store, name='create_task'),
    path('delete/<int:task_id>', views.delete, name='delete_task'),
    path('update/<int:task_id>', views.update, name='update_task'),
]
