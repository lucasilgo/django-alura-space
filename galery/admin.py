from django.contrib import admin
from galery.models import Photo

class ListPhoto(admin.ModelAdmin):
    list_display = ("id", "name", "caption")
    list_display_links = ("id", "name")
    search_fields = ("name",)

admin.site.register(Photo, ListPhoto)
