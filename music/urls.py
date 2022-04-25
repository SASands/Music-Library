from django.urls import path
from . import views

urlpatterns = [
    path('',views.songs_list),
    # path('music/<int:pk>/', views.songs_detail),
]