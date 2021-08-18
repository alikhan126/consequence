from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseTimeStampedModel(models.Model):
    """
    Abstract model that contains created_at, updated_at
    To be inherited by all other models
    """
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date Updated"), auto_now=True)

    class Meta:
        abstract = True
