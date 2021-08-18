from django.db import models
from common.models import BaseTimeStampedModel

from django.conf import settings

class TrueLayerAuth(BaseTimeStampedModel):
    access_token = models.TextField(max_length=50)
    refresh_token = models.TextField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="truelayer_accounts", on_delete=models.CASCADE)

    def __str__(self):
    	return f'{self.user}'


class Account(BaseTimeStampedModel):
    account_id = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    account_swift_bic = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    account_sort_code = models.CharField(max_length=50)
    provider_display_name = models.CharField(max_length=50)
    provider_id = models.CharField(max_length=50)
    provider_logo_uri = models.TextField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="bank_accounts", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.display_name}: {self.account_id}'


class AccountTransaction(BaseTimeStampedModel):
    description = models.TextField(blank=True)
    transaction_type = models.CharField(max_length=50, null=True, blank=True)
    currency = models.CharField(max_length=50)
    transaction_category = models.CharField(max_length=50)
    transaction_classification = models.TextField(null=True, blank=True)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    running_balance = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    transaction_id = models.CharField(max_length=50)
    provider_transaction_id = models.CharField(max_length=50)
    normalised_provider_transaction_id = models.TextField(null=True, blank=True)
    account = models.ForeignKey(Account, related_name="transactions", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account_id}: {self.transaction_id}'


class Card(BaseTimeStampedModel):
    account_id = models.CharField(max_length=50)
    card_network = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    partial_card_number = models.CharField(max_length=50)
    name_on_card = models.CharField(max_length=50)
    provider_display_name = models.CharField(max_length=50)
    provider_id = models.CharField(max_length=50)
    provider_logo_uri = models.TextField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="cards", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.display_name}: {self.card_network}'


