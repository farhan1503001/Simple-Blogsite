from django.urls import path
from .views import AddCategories, Postdetail, Postlist,Addpost,PostEdit,DeletePost, UserPost, category_detail, likeview
urlpatterns = [
    path('',Postlist.as_view(),name='home'),
    path('details/int:<pk>',Postdetail.as_view(),name='details'),
    path('add_post/',Addpost.as_view(),name='add_post'),
    path('details/update/int:<pk>',PostEdit.as_view(),name='edit'),
    path('details/int:<pk>/delete',DeletePost.as_view(),name='delete'),
    path('user_post/',UserPost.as_view(),name='userpost'),
    path('add_category/',AddCategories.as_view(),name='add_cat'),
    path('category/<str:cats>',category_detail,name='cat_details'),
    path('details/add_like/int:<pk>',likeview,name='add_like'),
]