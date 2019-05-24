from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, state_choices, bedroom_choices
from listings.models import Listing
from salesmen.models import Salesman


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(
        is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    salesmen = Salesman.objects.order_by('-hire_date')
    mvp_salesmen = Salesman.objects.all().filter(is_mvp=True)
    context = {'salesmen': salesmen, 'mvp_salesmen': mvp_salesmen}
    return render(request, 'pages/about.html', context)