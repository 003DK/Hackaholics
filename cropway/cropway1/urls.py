from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('choose-farm/', views.choose_farm_path, name='choose_farm'),
    path('land-farming/', views.land_farming_view, name='land_farming'),
    path('rooftop-farming/', views.rooftop_farming_view, name='rooftop_farming'), 
    path('farming/recommend/', views.recommend_crops, name='recommend_crops'),
]
