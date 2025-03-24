from django.urls import path
from .views import VideosListView

urlpatterns = [
    path('', VideosListView.as_view(), name='videos-list'),
]
