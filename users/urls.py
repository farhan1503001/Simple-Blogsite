from django.urls import path
from . views import profile_edit, user_register
urlpatterns = [
    path('register/',user_register.as_view(),name='register'),
    path('edit_profile/',profile_edit.as_view(),name='pedit')
]