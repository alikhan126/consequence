import json
import uuid
import urllib
import time
import requests
import jwt
import requests
import humanize

from datetime import datetime

from django.conf import settings

from true_layer.helpers.validators import validate_dtformat
from true_layer.models import Account, AccountTransaction, Card


class TrueLayerAPI:
	def __init__(self) -> None:
		self.client_id = settings.TRUELAYER_CLIENT_ID
		self.client_secret = settings.TRUELAYER_CLIENT_SECRET
		self.redirect_uri = settings.TRUELAYER_REDIRECT_URI
		self.headers = {}
		self.url = settings.TRUELAYER_AUTH_URI
		self.auth_url = f"{self.url}connect/token"
		self.data_api_uri = f"{self.url}data/v1"
		self.scope = "info cards accounts transactions balance offline_access direct_debits standing_orders products beneficiaries"
		self.access_token = None
		self.refresh_token = None
		self.credentials_id = None
		self.expiration_date = None
		super().__init__()

	def get_auth_url(self, state):
		query_param = urllib.parse.urlencode(
			{
				"response_type": "code",
				"client_id": self.client_id,
				# List of permissions https://docs.truelayer.com/#permissions
				"scope": self.scope,
				"nonce": int(time.time()),
				"redirect_uri": self.redirect_uri,
				"enable_mock": "true",
				"enable_open_banking_providers": "true",
				"enable_credentials_sharing_providers": "false",
				"state": state
			}
		)

		auth_uri = f"https://auth.truelayer-sandbox.com/?{query_param}"
		return auth_uri

	def from_code(self, code: str) -> None:
		result= self.exchange_code(code)
		return result

	def from_refresh_token(self, refresh_token: str) -> None:
		self.access_token, self.refresh_token = self._refresh_access_token(
			refresh_token
		)
		self._extract_info_from_token(access_token=self.access_token)

	def _extract_info_from_token(self, access_token: str) -> None:
		# The JWT is base64 encoded. We decode it and extract the infos inside it
		decoded = jwt.decode(access_token, verify=False)
		self.credentials_id = decoded["sub"]
		self.expiration_date = decoded["exp"]

	@property
	def lifetime(self) -> str:
		return humanize.naturaldelta(
			datetime.fromtimestamp(self.expiration_date) - datetime.now()
		)

	def refresh_access_token(self) -> None:
		if self.refresh_token is None:
			raise ValueError("We don't have a refresh token for this credentials!")
		self.access_token, self.refresh_token = self._refresh_access_token(
			self.refresh_token
		)

	def _exchange_authorization_code(self, code: str):
		params = {
			"grant_type": "authorization_code",
			"client_id": self.client_id,
			"client_secret": self.client_secret,
			"redirect_uri": self.redirect_uri,
			"code": code,
		}
		
		r = requests.post(self.auth_url, data=params)
		r.raise_for_status()
		body = r.json()
		return body["access_token"], body["refresh_token"]

	def _refresh_access_token(self, refresh_token: str):
		params = {
			"grant_type": "refresh_token",
			"client_id": self.client_id,
			"client_secret": self.client_secret,
			"refresh_token": refresh_token,
		}
		r = requests.post(self.auth_url, data=params)
		r.raise_for_status()
		body = r.json()
		return body["access_token"], body["refresh_token"]


	def exchange_code(self, code):
		params = {
			"grant_type": "authorization_code",
			"client_id": self.client_id,
			"client_secret": self.client_secret,
			"redirect_uri": self.redirect_uri,
			"code": code,
		}

		result = requests.post(self.auth_url, data=params, headers=self.headers)
		result = result.json()
		return result



class TrueLayerDataAPI:
	def __init__(self, token) -> None:
		self.client_id = settings.TRUELAYER_CLIENT_ID
		self.client_secret = settings.TRUELAYER_CLIENT_SECRET
		self.redirect_uri = settings.TRUELAYER_REDIRECT_URI
		self.headers = {}
		self.headers["Authorization"] = f'Bearer {token}'
		self.url = settings.TRUELAYER_URI
		self.auth_url = f"{self.url}connect/token"
		self.data_api_uri = f"{self.url}data/v1"

		super().__init__()

	def __save_account(sefl, user, result):
		payload = {
			"account_id": result['account_id'],
			"account_type": result['account_type'],
			"display_name": result['display_name'],
			"currency": result['currency'],
			"account_swift_bic": result['account_number']['swift_bic'],
			"account_number": result['account_number']['number'],
			"account_sort_code": result['account_number']['sort_code'],
			"provider_display_name": result['provider']['display_name'],
			"provider_id": result['provider']['provider_id'],
			"provider_logo_uri": result['provider']['logo_uri'],
		}
		account = Account.objects.filter(account_id=payload['account_id'], user_id=user)
		if account:
			account.update(**payload)
		else:
			payload['user_id'] = user
			account, created = Account.objects.get_or_create(**payload)
		return account

	def __save_card_detail(self, user, result):
		payload = {
			"account_id": result['account_id'],
			"card_network": result['card_network'],
			"card_type": result['card_type'],
			"currency": result['currency'],
			"display_name": result['display_name'],
			"partial_card_number": result['partial_card_number'],
			"name_on_card": result['name_on_card'],
			"provider_display_name": result['provider']['display_name'],
			"provider_id": result['provider']['provider_id'],
			"provider_logo_uri": result['provider']['logo_uri'],
		}
		payload['user_id'] = user
		card, created = Card.objects.get_or_create(**payload)
		return card

	def __save_account_transaction(self, account_id, result):
		account = Account.objects.get(account_id=account_id)

		payload = {
			"description": result['description'],
			"transaction_type": result['transaction_type'],
			"transaction_category": result['transaction_category'],
			"transaction_classification": result['transaction_classification'],
			"amount": result['amount'],
			"currency": result['currency'],
			"transaction_id": result['transaction_id'],
			"provider_transaction_id": result['provider_transaction_id'] if 'provider_transaction_id' in result else "",
			"normalised_provider_transaction_id": result['normalised_provider_transaction_id'] if 'normalised_provider_transaction_id' in result else "",
			"running_balance": result['running_balance']['amount']
		}

		payload['account_id'] = account.id
		account_transaction, created = AccountTransaction.objects.get_or_create(**payload)
		return account_transaction

	def get_accounts(self, user):
		url = f"{self.data_api_uri}/accounts"

		r = requests.get(url, headers=self.headers)
		r.raise_for_status()
		body = r.json()

		if body["status"] == "Succeeded":
			results = body["results"]
			for result in results:
				self.__save_account(user, result)
			return results
		else:
			return []

	def get_user_info(self):
		url = f"{self.data_api_uri}/info"
		r = requests.get(url, headers=self.headers)
		r.raise_for_status()
		body = r.json()
		if body["status"] == "Succeeded":
			results = body["results"]
			return results
		else:
			return []

	def get_balance(self, account_id: str):
		url = f"{self.data_api_uri}/accounts/{account_id}/balance"
		r = requests.get(url, headers=self.headers)
		body = r.json()
		
		if body["status"] == "Succeeded":
			results = body["results"]
			return results[0]
		else:
			return []

	def get_account_transactions(self, user, account_id, txn_from=None, txn_to=None):
		"""
		:param txn_from: YYYY-MM-DD
		:param txn_to: YYYY-MM-DD
		"""
		if txn_from:
			validate_dtformat(txn_from)
		if txn_to:
			validate_dtformat(txn_to)

		url = f"{self.data_api_uri}/accounts/{account_id}/transactions"
		payload = {"from": txn_from, "to": txn_to}
		r = requests.get(url, headers=self.headers, params=payload)
		
		body = r.json()
		if body["status"] == "Succeeded":
			results = body["results"]
			for result in results:
				self.__save_account_transaction(account_id, result)
			return results
		else:
			return []

	def get_cards(self, user):
		url = f"{self.data_api_uri}/cards"

		r = requests.get(url, headers=self.headers)
		r.raise_for_status()
		body = r.json()
		if body["status"] == "Succeeded":
			results = body["results"]
			for result in results:
				self.__save_card_detail(user, result)
			return results
		else:
			return []

	def get_card_transactions(self, card_id):
		url = f"{self.data_api_uri}/cards/{card_id}/transactions"

		r = requests.get(url, headers=self.headers)
		r.raise_for_status()
		body = r.json()
		if body["status"] == "Succeeded":
			results = body["results"]
			return results
		else:
			return []
