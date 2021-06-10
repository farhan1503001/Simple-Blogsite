from django.urls import path
from .views import Postdetail, Postlist,Addpost
urlpatterns = [
    path('',Postlist.as_view(),name='home'),
    path('details/int:<pk>',Postdetail.as_view(),name='details'),
    path('add_post/',Addpost.as_view(),name='add_post'),
]