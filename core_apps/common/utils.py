from django.utils.text import slugify
from django.template.loader import render_to_string
import os
import random
import uuid


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,909982308340)
    name, ext  = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename = new_filename, ext = ext)
    return "products/{new_filename}/{final_filename}".format(new_filename='products', final_filename=final_filename)



def random_string_generator():
    return str(uuid.uuid4()).replace('-','')

# def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

def unique_order_id_generator(instance):

    """
    This is for a Django project With an order_id field
    """
    order_new_id = random_string_generator()
    
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return order_new_id

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

