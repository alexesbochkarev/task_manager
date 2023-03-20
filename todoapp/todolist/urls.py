from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('complete/', views.CompleteListView.as_view(), name='complete'),
    path('notcomplete/', views.CompleteNotListView.as_view(), name='notcomplete'),
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('search_number/', views.SearchNumberView.as_view(), name='search_number'),
    path('search_date/', views.SearchDateView.as_view(), name='search_date'),
    path('detail/<int:pk>', views.TodoDetailview.as_view(), name='detail'),
    path('update_comment/<int:pk>', views.TodoUpdateView.as_view(), name='update_comment'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
