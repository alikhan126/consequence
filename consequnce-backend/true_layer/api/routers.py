from django.conf.urls import url
from rest_framework import routers
from django.urls import path, include

from true_layer.api.viewsets import (
    TrueLayerAuthView,
    TrueLayerCallback,
    TrueLayerAccounts,
    TrueLayerInfo,
    TrueLayerTransactions,
    TrueLayerBalance,
    TrueLayerCards,
    TrueLayerCardTransactions
)

router = routers.SimpleRouter()

urlpatterns = [
    url(r'', include(router.urls)),
    path('sign-in/', TrueLayerAuthView.as_view(), name='truelayer_sign_in'),
    path('callback/', TrueLayerCallback.as_view(), name='truelayer_callback'),
    path('accounts/', TrueLayerAccounts.as_view(), name='truelayer_accounts'),
    path('info/', TrueLayerInfo.as_view(), name='truelayer_info'),
    path('balance/', TrueLayerBalance.as_view(), name='truelayer_balance'),
    path('transactions/', TrueLayerTransactions.as_view(), name='truelayer_transactions'),
    path('cards/', TrueLayerCards.as_view(), name='truelayer_cards'),
    path('card/transactions/', TrueLayerCardTransactions.as_view(), name='truelayer_card_transactions'),
]
