import os

from django.core.cache import cache

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
SHEET_NAME = os.getenv("SHEET_NAME")
RANGE_NAME = SHEET_NAME

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), '..', 'credentials.json')

CACHE_KEY = 'google_sheet_data'
CACHE_TIMEOUT = float(os.getenv("CACHE_TIMEOUT"))


def get_sheet_service():
	credentials = Credentials.from_service_account_file(
		SERVICE_ACCOUNT_FILE,
		scopes=SCOPES
	)
	service = build('sheets', 'v4', credentials=credentials)
	return service.spreadsheets()


def fetch_sheet_data():
	cached_data = cache.get(CACHE_KEY)
	if cached_data:
		return cached_data

	sheet = get_sheet_service()
	result = sheet.values().get(
		spreadsheetId=SPREADSHEET_ID,
		range=RANGE_NAME
	).execute()
	values = result.get('values', [])
	cache.set(CACHE_KEY, values, CACHE_TIMEOUT)
	return values


def get_student_scores(username):
	values = fetch_sheet_data()

	if not values or len(values) < 2:
		return None

	headers = values[0]

	for row in values[1:]:
		if row and row[0].strip().lower() == username.lower():
			row += [""] * (len(headers) - len(row))
			return dict(zip(headers, row))

	return None
