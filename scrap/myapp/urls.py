from django.urls import path
from . import views

urlpatterns = [
    path('scrape', views.scrape, name='scrape'),
    path('download/<str:pk>', views.download, name='download'),
    path('content/<int:pk>/', views.content, name='content'),
    path('look/<int:pk>/', views.look, name='look'),


]
