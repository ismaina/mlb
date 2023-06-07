from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .forms import ContactForm

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# @cache_page(CACHE_TTL)
def index(request):
    return render(request, 'index.html')


def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        print(request.POST, '\n\n\n\n\n\n\n\n')
        if form.is_valid():
            form.save()
            context['form'] = form
            context['success'] = form.instance
            return render(request, 'contact/contactform.html', context)
    else:
        form = ContactForm(request.POST or None, request.FILES or None)
    context['form'] = form
    return render(request, 'contact/contactform.html', context)

def about(request):
    context = {}
    return render(request, 'contact/aboutus.html', context)

# @cache_page(CACHE_TTL)
def heritage(request):
    context = {}
    return render(request, 'heritage.html', context)