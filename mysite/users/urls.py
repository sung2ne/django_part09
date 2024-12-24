from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.users_list, name='list'),
    path('<int:user_id>/', views.users_read, name='read'),
    path('<int:user_id>/delete/', views.users_delete, name='delete'),
]
