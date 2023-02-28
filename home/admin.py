from django.contrib import admin
from .models import GalleryArt

class ListaGalleryArt(admin.ModelAdmin):
    list_display = ('title', 'date_create' )

admin.site.register(GalleryArt, ListaGalleryArt)