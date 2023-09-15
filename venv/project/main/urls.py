from django.urls import path,include
from .views import landing_view,home_view,list_view,listing_view,like_listing_view
from django.contrib import admin

urlpatterns=[
    path( '',landing_view,name='main' ),

     path( 'home/',home_view,name='home' ),

    path( 'list/',list_view,name='list' ),

    path( 'listing/<str:id>/',listing_view,name='listing' ),

    path ('listing/<str:id>/like/',like_listing_view,name='like' )



]