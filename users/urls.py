from django.urls import path
from . views import password_change_view, profile_edit, user_register
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',user_register.as_view(),name='register'),
    path('edit_profile/',profile_edit.as_view(),name='pedit'),
    path('password/',password_change_view.as_view())
]