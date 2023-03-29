from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


# class Profile(models.Model):
#     user = models.ForeignKey(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE, related_name='profile', unique=True)

#     def __str__(self) -> str:
#         return str(self.user)
    

class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE, related_name='profile', unique=True)

    CHOICES = (
        (False, _('Nitflex')),
        (False, _('HPO')),
        (False, _('Disnep')),
    )

    choice_1 = models.BooleanField(_('Nitflex'), default=False)
    choice_2 = models.BooleanField(_('HPO'), default=False)
    choice_3 = models.BooleanField(_('Disnep'), default=False)

    def __str__(self) -> str:
        return str(self.user)
