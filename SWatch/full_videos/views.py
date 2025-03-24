from django.shortcuts import render
from .models import Channel, Video
from django.views.generic import ListView


class VideosListView(ListView):
    model = Video
    template_name = "main.html"  # Вказуємо конкретний шаблон
    context_object_name = "videos"
    ordering = ["-upload_date"]
    paginate_by = 10