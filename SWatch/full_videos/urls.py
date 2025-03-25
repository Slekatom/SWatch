from django.urls import path
from .views import VideosListView, VideosDetailView, follow, view

urlpatterns = [
    path('', VideosListView.as_view(), name='videos-list'),
    path('video/<int:pk>/watch/', VideosDetailView.as_view(), name="video-detail"),
    path('channel/<int:pk>/', VideosDetailView.as_view(), name='channel-detail'),
    path('channel/<int:pk>/follow/', follow, name='follow'),
    path('video/<int:pk>/watch/view/', view, name='view'),
]