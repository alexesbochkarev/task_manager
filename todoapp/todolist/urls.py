from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('complete/', views.CompleteListView.as_view(), name='complete'),
    path('notcomplete/', views.CompleteNotListView.as_view(), name='notcomplete'),
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('search_number/', views.SearchNumberView.as_view(), name='search_number'),
    path('search_date/', views.SearchDateView.as_view(), name='search_date'),
    path('detail/<int:pk>', views.todo_detail, name='detail'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
