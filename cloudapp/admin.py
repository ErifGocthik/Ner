from django.contrib import admin

# Register your models here.
from cloudapp.models import Image, Archive


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    exclude = ['id']
    list_display = ['name', 'file_size', 'get_size', 'user_id']


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    exclude = ['id']
    list_display = ['name']