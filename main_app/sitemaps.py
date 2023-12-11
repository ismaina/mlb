from django.contrib.sitemaps import Sitemap
from core_apps.products.models import Product


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_at