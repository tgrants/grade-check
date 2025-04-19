# GradeCheck

This app allows students to check their scores stored in a google sheets spreadsheet,
without giving direct access to it.

## Setup

### Development

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py createsuperuser`
- `python manage.py collectstatic`
- `python manage.py runserver`

### Production

- Download and place your `credentials.json` in this directory
- Set environment variables
	- Copy template `cp .env.example .env`
	- Edit it `nano .env`
- Build and start container `docker-compose up --build`

## Contributing

Contributions are welcome.
For more information see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

This project is licensed under the terms of the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
See the [LICENSE](LICENSE) file for more information.
