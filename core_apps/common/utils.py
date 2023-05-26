import os
import random


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
    return "feedback/{new_filename}/{final_filename}".format(new_filename='feedback', final_filename=final_filename)