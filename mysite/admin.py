from django.contrib import admin
from mysite.models import PlayList, video

class videoAdmin(admin.ModelAdmin):
    list_display = ('title', 'vid', 'plist')
 
admin.site.register(PlayList)
admin.site.register(video, videoAdmin)
