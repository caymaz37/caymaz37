from django.urls import path
from django.conf import settings
from . import views 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('detail', views.detail, name='detail'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('hp_toner', views.toner_list_by_brand_and_model, name='hp_toner'),
    path('product/<int:id>/', views.detail, name='detail'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)