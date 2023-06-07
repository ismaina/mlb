from django.contrib.sitemaps import Sitemap
from core_apps.products.models import Product


class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_at