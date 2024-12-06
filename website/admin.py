from django.contrib import admin

from .models import Toner, SliderModel, TonerResim

class TonerResimInline(admin.TabularInline):
    model = TonerResim
    extra = 1  # Yeni toner eklerken bir resim için boş alan bırakır

@admin.register(Toner)
class TonerAdmin(admin.ModelAdmin):
    list_display = ('marka', 'model', 'fiyat')
    search_fields = ('marka', 'model')
    list_filter = ('marka',)

@admin.register(TonerResim)
class TonerResimAdmin(admin.ModelAdmin):
    list_display = ('toner', 'resim')

@admin.register(SliderModel)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'resim', 'aciklama')
  