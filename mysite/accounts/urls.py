from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('signup/', views.accounts_signup, name='signup'),
    path('login/', views.accounts_login, name='login'),
    path('logout/', views.accounts_logout, name='logout'),
    path('profile/', views.accounts_profile, name='profile'),
    path('update-profile/', views.accounts_update_profile, name='update_profile'),
    path('update-password/', views.accounts_update_password, name='update_password'),
    path('find-username/', views.accounts_find_username, name='find_username'),
    path('reset-password/', views.accounts_reset_password, name='reset_password'),
    path('delete-account/', views.accounts_delete_account, name='delete_account'),
]
