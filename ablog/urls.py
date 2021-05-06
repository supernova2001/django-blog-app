from django.contrib import admin
from django.urls import path,include
from . import views 
from .views import Home,Detailview,AddPost
urlpatterns = [
    #path('',views.Home,name="home"),
    path('',Home.as_view(),name='home'),
    path('details/<int:pk>',Detailview.as_view(),name='details'),
    path('add-post',AddPost.as_view(),name='add-post')
]
