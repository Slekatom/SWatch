from django.contrib import admin
from .models import Channel, Video, Following

admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(Following)