from django.db import models

class Channel(models.Model):
    COUNTRIES = [
        ("ua", "Ukraine"),
        ("us", "USA"),
        ("ge", "Germany"),
        ("fr", "France"),
        ("uk", "United Kingdom"),
        ("404", "Non defined")
    ]

    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    followers = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=20, choices=COUNTRIES, default="404")
    avatar = models.FileField(upload_to="avatars/", null=True, blank = True)

    def __str__(self):
        return f"Channel: {self.title}, Country: {self.country}"


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    path = models.FileField(upload_to="videos/", null=True, blank=True)
    photo = models.FileField(upload_to="photos/", null = True, blank = True)

    def __str__(self):
        return f"Video: {self.title}, Channel: {self.channel.title}"
