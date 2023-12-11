from typing import Any
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404, HttpRequest, HttpResponse
from .models import Product
import json

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
 
#  @cache_page(CACHE_TTL)

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'products/list.html'
    paginate_by = 8
    # cache_page

    # @method_decorator(cache_page(CACHE_TTL))
    # @method_decorator(vary_on_cookie)
    
    def get_queryset(self):
        qs = Product.objects.prefetch_related().all()
        if 'product' in cache:
            products = cache.get('product')
            return qs
        else:
            # store in cache
            # results = json.loads(serialize('json', qs))
            results = json.dumps(serialize('json', qs))
            cache.set('product', results, timeout=CACHE_TTL)
            return qs
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        
        return context
    

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.prefetch_related().all()
    template_name = 'products/detail.html'
    # template_name = 'snippets/product_category.html'
    # paginate_by = 2

    def get_context_data(self, *args,**kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        # print(instance,"hapa")

        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Product Does Not Exist")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance= qs.first()
        except:
            raise Http404("Wacha ufala")
        return instance