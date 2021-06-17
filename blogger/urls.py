from django.urls import path
from .views import Postdetail, Postlist,Addpost,PostEdit,DeletePost, UserPost,likeview
urlpatterns = [
    path('',Postlist.as_view(),name='home'),
    path('details/int:<pk>',Postdetail.as_view(),name='details'),
    path('add_post/',Addpost.as_view(),name='add_post'),
    path('details/update/int:<pk>',PostEdit.as_view(),name='edit'),
    path('details/int:<pk>/delete',DeletePost.as_view(),name='delete'),
    path('user_post/',UserPost.as_view(),name='userpost'),
    path('add_like/int:<pk>',likeview,name='like'),
]