from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from core_apps.common.models import TimeStampedUUIDModel, AbstractManager
User = get_user_model()


class PartnerManager(AbstractManager):
    
    def get_pm(self):
        return super().get_queryset().filter(role=Profile.Role.PM)
    

class Profile(TimeStampedUUIDModel):
    class Gender(models.TextChoices):
        MALE = "male", _("male")
        FEMALE = "female", _("female")
        OTHER = "other", _("other")
    class Role(models.TextChoices):
        ADMIN = "admin", _("admin")
        ANALYST = "analyst", _("analyst")
        PM = "Project Manager", _("Project Manager")
        PARTNER = "Partner", _("Partner")
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    pms = PartnerManager()
    
    about_me = models.TextField(
        verbose_name=_("about me"),
        default="say something about yourself",
    )
    gender = models.CharField(
        verbose_name=_("gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    role = models.CharField(
        verbose_name=_("role"),
        choices=Role.choices,
        default=Role.PM,
        max_length=20,
    )
    profile_photo = models.ImageField(
        verbose_name=_("profile photo"), default="/profile_default.png"
    )
    
    def __str__(self):
        # return f"{self.user}"
        return f"{self.user.get_full_name}"