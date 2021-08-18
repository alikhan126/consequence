from django.db import models
from common.models import BaseTimeStampedModel

from django.conf import settings

class TrueLayerAuth(BaseTimeStampedModel):
    access_token = models.TextField(max_length=50)
    refresh_token = models.TextField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="truelayer_accounts", on_delete=models.PROTECT)

    def __str__(self):
    	return f'{self.user}'