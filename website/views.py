from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Toner, SliderModel

def index(request):
    products = Toner.objects.all()
    sliders = SliderModel.objects.all()
    return render(request, 'website/index.html', {
        'products': products,
        'sliders': sliders,
        
        })


def toner_list_by_brand_and_model(request, marka, model):
    # Marka ve modele göre ürünleri filtreleyin
    toners = Toner.objects.filter(marka=marka, model=model)
    return render(request, 'website/hp_toner.html', {'toners': toners, 'marka': marka, 'model': model})


def contact(request):
    return render(request, 'website/contact.html')


def shop(request):
    products = Toner.objects.all()
    return render(request, 'website/shop.html', {'products': products})


def cart(request):
    return render(request, 'website/cart.html')





def detail(request, id):
    product = get_object_or_404(Toner, id=id)
    return render(request, 'website/detail.html', {'product': product})