from django.contrib import admin
from true_layer.models import TrueLayerAuth, Account, AccountTransaction, Card

admin.site.register(TrueLayerAuth)
admin.site.register(Account)
admin.site.register(AccountTransaction)
admin.site.register(Card)
