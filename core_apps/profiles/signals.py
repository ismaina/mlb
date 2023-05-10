import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from main_app.settings.base import AUTH_USER_MODEL
from core_apps.profiles.models import Profile

from django.core.mail import mail_admins
from django.http import HttpResponse

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print(sender,instance, kwargs)
        logger.info(f"{instance}'s profile created")
        email = instance.profile.user.email
        organization = instance.profile.user.email
        msg = f'Success account creation for user {email}'
        # res = mail_admins('TES Taarifa Mail', msg)
        # return HttpResponse('%s'%res)


# @receiver(post_save, sender=AUTH_USER_MODEL)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
#     logger.info(f"{instance}'s profile created")
    
#     email = instance.profile.user.email
#     msg = f'Success account creation for user {email}'
#     res = mail_admins('TES Taarifa Mail', msg)
#     return HttpResponse('%s'%res)
    


# @receiver(post_save, sender=AUTH_USER_MODEL)
# def sendAdminsEmail(sender, instance, *args, **kwargs):
#     email = instance.profile.user.email
#     msg = f'Success account creation for user {email}'
#     res = mail_admins('TES Taarifa Mail', msg)
#     return HttpResponse('%s'%res)