import os
import pickle
from datetime import datetime, timedelta
from django.core.cache import cache
from decouple import config

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SPREADSHEET_ID = config('SPREADSHEET_ID')
SHEET_NAME = config('SHEET_NAME')
RANGE_NAME = f"{SHEET_NAME}!A1:Z"

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), '..', 'credentials.json')

CACHE_KEY = 'google_sheet_data'
CACHE_TIMEOUT = config('CACHE_TIMEOUT')


def get_sheet_service():
	credentials = Credentials.from_service_account_file(
		SERVICE_ACCOUNT_FILE,
		scopes=SCOPES
	)
	service = build('sheets', 'v4', credentials=credentials)
	return service.spreadsheets()


def fetch_sheet_data():
	sheet = get_sheet_service()
	result = sheet.values().get(
		spreadsheetId=SPREADSHEET_ID,
		range=RANGE_NAME
	).execute()
	values = result.get('values', [])
	cache.set(CACHE_KEY, values, CACHE_TIMEOUT)
	return values


def get_student_scores(username):
	sheet = get_sheet_service()
	result = sheet.values().get(
		spreadsheetId=SPREADSHEET_ID,
		range=RANGE_NAME
	).execute()

	values = result.get('values', [])
	if not values or len(values) < 2:
		return None

	headers = values[0]

	for row in values[1:]:
		if row and row[0].strip().lower() == username.lower():
			row += [""] * (len(headers) - len(row))
			return dict(zip(headers, row))

	return None
