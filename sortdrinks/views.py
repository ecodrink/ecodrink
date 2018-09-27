from django.db.models import Q
from django.shortcuts import render

from .forms import DrinkForm, FuzzyDrinkForm
from .models import Drink


def index(request):
    """Index page and a very naive search view.

    Include everything it can from the string provided by the user.
    """
    form = FuzzyDrinkForm(request.GET or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        query = form.cleaned_data['q']
        max_results = form.cleaned_data['length']
        keywords = query.split()
        drinks = Drink.objects.all()
        for keyword in keywords:
            drinks = drinks.filter(Q(category__name__icontains=keyword) |
                                   Q(style__name__icontains=keyword))
        context['drinks'] = drinks[:max_results]
    return render(request, 'sortdrinks/index.html', context)


def search(request):
    """Precise search."""
    form = DrinkForm(request.GET or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        max_results = form.cleaned_data['length']
        categories = form.cleaned_data['categories']
        styles = form.cleaned_data['styles']
        countries = form.cleaned_data['countries']
        organic = form.cleaned_data['organic']
        drinks = Drink.objects.all()
        if categories:
            drinks = drinks.filter(category__in=categories)
        if styles:
            drinks = drinks.filter(style__in=styles)
        if countries:
            drinks = drinks.filter(country__in=countries)
        if organic:
            drinks = drinks.filter(organic=organic)
        context['drinks'] = drinks[:max_results]
    return render(request, 'sortdrinks/index.html', context)
