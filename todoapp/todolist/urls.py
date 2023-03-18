from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
