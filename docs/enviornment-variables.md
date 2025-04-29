# Environment variables

## Spreadsheet

- `SPREADSHEET_ID`
	- The ID of the spreadsheet you want to share
	- You can extract it from the URL
	- Example value: `1tAD7xkj3GdSL1xnRlA4UJXCKO_71pzwiVKY8Fkr-XY4`
- `SHEET_NAME`
	- The name of the page you want to share
	- Located at the bottom of the spreadsheet
	- Example value: `Sheet1`
- `CACHE_TIMEOUT`
	- Time in seconds before the sheet cache expires
	- Caching is done to reduce the amount of requests to the API
	- Example value: `300` (5 minutes)

## Django

- `DJANGO_SECRET_KEY`
	- Secret key used for cryptographic signing
	- Default value: generated automatically when the app is run for the first time
	- Example value: `uWZOXv1Tl10ZXpxEUe-xPB10RlYz05YRTpjpvnQQHqTGOg2C5TZxvuEiKKOphYbJUHs`

## Postgres

- `POSTGRES_DB`
	- Name for the postgres database
	- Example value: `gcdb`
- `POSTGRES_USER`
	- Username for the postgres user
	- Example value: `gcuser`
- `POSTGRES_PASSWORD`
	- Password for the postgres user
	- Example value: `gcpass`
- `POSTGRES_HOST`
	- Host address for the postgres database
	- Default value: `localhost`

## Default admin

- `DEFAULT_ADMIN_USERNAME`
	- Username for the initial admin user
	- Default value: `admin`
- `DEFAULT_ADMIN_PASSWORD`
	- Password for the initial admin user
	- Default value: `gradecheck`
