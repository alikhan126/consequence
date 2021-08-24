import time
from django.conf import settings

from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from true_layer.helpers.truelayer import TrueLayerAPI, TrueLayerDataAPI
from true_layer.models import TrueLayerAuth, Account, Card
from true_layer.api.serializers import AccountSerializer, CardSerializer
from user.models import User


class TrueLayerCardsViewset(viewsets.ModelViewSet):
    """
    Viewset to create, list, update and delete VideoRoom.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated,)



class TrueLayerAccountsViewset(viewsets.ModelViewSet):
    """
    Viewset to list accounts
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)


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
		self.__save_tokens(user_id, result)
		return Response(result, status=status.HTTP_200_OK)

	def __save_tokens(self, user_id, result):
		user = User.objects.get(id=user_id)
		true_layer_auth =  TrueLayerAuth.objects.filter(user=user)
		if true_layer_auth:
			true_layer_auth.update(
				access_token=result['access_token'],
				refresh_token=result['refresh_token']
			)
		else:
			true_layer_auth, created = TrueLayerAuth.objects.get_or_create(
				user=user, access_token=result['access_token'],
				refresh_token=result['refresh_token']
			)
		return True


class TrueLayerAccounts(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		token = TrueLayerAuth.objects.get(user__id=request.user.id)
		result = TrueLayerDataAPI(token=token.access_token).get_accounts(request.user.id)
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
		"""
		:param account_id: 433332233
		:param txn_from: YYYY-MM-DD
		:param txn_to: YYYY-MM-DD
		"""
		account_id = request.query_params.get("account_id")
		txn_from = request.query_params.get("from", None)
		txn_to = request.query_params.get("to", None)

		if account_id:
			token = TrueLayerAuth.objects.get(user__id=request.user.id)
			result = TrueLayerDataAPI(token=token.access_token).get_account_transactions(
				request.user.id, account_id, txn_from, txn_to
			)
		else:
			token = TrueLayerAuth.objects.get(user__id=request.user.id)
			accounts = Account.objects.filter(user=request.user)
			for account in accounts:
				result = TrueLayerDataAPI(token=token.access_token).get_account_transactions(
					request.user.id, account.account_id, txn_from, txn_to
				)
		return Response(result, status=status.HTTP_200_OK)


class TrueLayerCards(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		token = TrueLayerAuth.objects.get(user__id=request.user.id)
		result = TrueLayerDataAPI(token=token.access_token).get_cards(request.user.id)
		return Response(result, status=status.HTTP_200_OK)


class TrueLayerCardTransactions(APIView):
	permission_classes = (AllowAny,)

	def get(self, request):
		"""
		:param card_id: 433332233
		"""
		card_id = request.query_params.get("card_id")

		token = TrueLayerAuth.objects.get(user__id=request.user.id)
		result = TrueLayerDataAPI(token=token.access_token).get_card_transactions(card_id)
		return Response(result, status=status.HTTP_200_OK)



