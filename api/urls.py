from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.api_views, name='api_views'),
    path("task-list/", views.task_list, name='task-list'),
    path("detail-view/<str:pk>", views.detail_view, name='task-list'),
    path("create-view", views.crate_task, name='crate_task'),
    path("update-view/<str:pk>", views.update_task, name='update_task'),
    path("delete_task/<str:pk>", views.delete_task, name='delete_task'),
]
