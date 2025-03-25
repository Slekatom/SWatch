from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Channel, Video, Following, View
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Count, Case, When, IntegerField

class VideosListView(ListView):
    model = Video
    template_name = "main.html"  # Вказуємо конкретний шаблон
    context_object_name = "videos"
    ordering = ["-upload_date"]
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            watched_videos = View.objects.filter(user=user).values_list("video_id", flat=True)
            return Video.objects.annotate(
                is_watched=Case(
                    When(id__in=watched_videos, then=1),
                    default=0,
                    output_field=IntegerField(),
                )
            ).order_by("is_watched", "-upload_date")

        return Video.objects.order_by("-upload_date")

class VideosDetailView(DetailView):
    model = Video
    template_name = "detail.html"
    context_object_name = "video"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = context['video']

        is_following = Following.objects.filter(channel=video.channel, user=self.request.user).exists()

        context['is_following'] = is_following

        return context


@login_required
def follow(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    following, created = Following.objects.get_or_create(channel=channel, user=request.user)

    if not created:
        following.delete()
        created = False
    else:
        created = True

    request.session['follow_status'] = created  # Збережемо стан у сесії
    return redirect('video-detail', pk=channel.pk)

@login_required
def view(request, pk):
    video = get_object_or_404(Video, id=pk)
    _, created = View.objects.get_or_create(video = video, user = request.user)

    request.session['follow_status'] = created
    return redirect('video-detail', pk=video.pk)


