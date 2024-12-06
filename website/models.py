from django.db import models
from django.contrib.auth.models import User


class Toner(models.Model):
    marka = models.CharField(max_length=100, verbose_name="Marka")
    model = models.CharField(max_length=100, verbose_name="Model")
    resim = models.ImageField(upload_to="toner_resimleri/", verbose_name="Resim", blank=True, null=True)
    aciklama = models.TextField(verbose_name="Açıklama", blank=True)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat (TL)")

    class Meta:
        verbose_name = "Toner"
        verbose_name_plural = "Tonerler"
        ordering = ['marka', 'model']  # Markaya ve modele göre sıralar

    def __str__(self):
        return f"{self.marka} {self.model}"


class TonerResim(models.Model):
    toner = models.ForeignKey(Toner, on_delete=models.CASCADE, related_name="resimler", verbose_name="Toner")
    resim = models.ImageField(upload_to="toner_resimleri/", verbose_name="Toner Resmi")

    class Meta:
        verbose_name = "Toner Resmi"
        verbose_name_plural = "Toner Resimleri"

    def __str__(self):
        return f"{self.toner.marka} - Resim"


class SliderModel(models.Model):
    baslik = models.CharField(max_length=200, verbose_name="Başlık")
    resim = models.ImageField(upload_to="slider_resimleri/", verbose_name="Slider Resmi")
    aciklama = models.TextField(verbose_name="Açıklama", blank=True, null=True)
    aktif = models.BooleanField(default=True, verbose_name="Aktif Mi?")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliderlar"
        ordering = ['-olusturulma_tarihi']  # En yeni sliderlar önce listelenir

    def __str__(self):
        return self.baslik