from django.db import models
from django.db.models import Q
from core_apps.common.models import TimeStampedUUIDModel
from django.db.models.signals import pre_save
from core_apps.common.utils import upload_image_path, unique_slug_generator


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)
    
    def search(self, query):
        
        lookups = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(tag__title__icontains=query) 
            )
        return self.filter(lookups).distinct()
    


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset().active()
    def features(self):
        # return self.get_queryset().filter(featured=True)
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
    def search(self, query):
        return self.get_queryset().active().search(query)
    

class Product(TimeStampedUUIDModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=50, blank=True, null=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    code = models.IntegerField(blank=True, null=True, default=0000)
    datetime = models.DateTimeField( blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f"{self.title}"


class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    products = models.ManyToManyField(Product,blank=True)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    datetime = models.DateTimeField( blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = 'mlb'
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)