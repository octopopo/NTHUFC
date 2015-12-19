from django.contrib import admin
from photos.models import Photo, Tag
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('id','title');
	
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Tag)

