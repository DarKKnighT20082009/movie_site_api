from django.urls import path
from .views import UserDetailView, UserListView

urlpatterns = [
    path('<str:username>/', UserDetailView.as_view(), name='user-detail'),
    path('', UserListView.as_view(), name='user-list'),
]