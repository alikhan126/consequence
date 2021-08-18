import time
from django.conf import settings

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from true_layer.helpers.truelayer import TrueLayerAPI, TrueLayerDataAPI
from true_layer.models import TrueLayerAuth
from user.models import User


class TrueLayerAuthView(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		auth_uri = TrueLayerAPI().get_auth_url(state=request.user.id)
		return Response({'redirect_uri': auth_uri}, status=status.HTTP_200_OK)


class TrueLayerCallback(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		authorization_code = request.GET.get("code")
		user_id = request.GET.get("state")
		result = TrueLayerAPI().from_code(authorization_code)

		user = User.objects.get(id=user_id)
		true_layer_auth, created = TrueLayerAuth.objects.get_or_create(
			user=user, access_token=result['access_token'],
			refresh_token=result['refresh_token']
		)
		return Response(result, status=status.HTTP_200_OK)


class TrueLayerAccounts(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		token = TrueLayerAuth.objects.get(user__id=request.user.id)
		result = TrueLayerDataAPI(token=token.access_token).get_accounts()
		return Response(result, status=status.HTTP_200_OK)


class TrueLayerInfo(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		token = TrueLayerAuth.objects.get(user__id=request.user.id)
		result = TrueLayerDataAPI(token=token.access_token).get_user_info()
		return Response(result, status=status.HTTP_200_OK)


class TrueLayerBalance(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		account_id = request.query_params.get("account_id")
		token = TrueLayerAuth.objects.get(user__id=request.user.id)
		result = TrueLayerDataAPI(token=token.access_token).get_balance(account_id=account_id)
		return Response(result, status=status.HTTP_200_OK)


class TrueLayerTransactions(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		account_id = request.query_params.get("account_id")
		txn_from = request.query_params.get("from", None)
		txn_to = request.query_params.get("to", None)

		token = TrueLayerAuth.objects.get(user__id=request.user.id)
		result = TrueLayerDataAPI(token=token.access_token).get_account_transactions(account_id, txn_from, txn_to)
		return Response(result, status=status.HTTP_200_OK)


class TrueLayerCards(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		token = TrueLayerAuth.objects.get(user__id=request.user.id)
		result = TrueLayerDataAPI(token=token.access_token).get_cards()
		return Response(result, status=status.HTTP_200_OK)


class TrueLayerCardTransactions(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		card_id = request.query_params.get("card_id")

		token = TrueLayerAuth.objects.get(user__id=request.user.id)
		result = TrueLayerDataAPI(token=token.access_token).get_card_transactions(card_id)
		return Response(result, status=status.HTTP_200_OK)



