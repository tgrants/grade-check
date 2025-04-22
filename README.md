# GradeCheck

This app allows educators to share scores from a google spreadsheet, without giving students direct access to it.

## Setup

Quick setup instructions for Linux.
For more detailed instructions, see the [documentation](docs/).

### General

- Prepare [Google sheets](https://workspace.google.com/products/sheets/)
	- Create a project in [Google Cloud console](https://console.cloud.google.com)
		- Enable Google Sheets API
		- Create a service account
	- Create your sheet (see [docs/sheet-format.md](docs/sheet-format.md))
	- Download and place your `credentials.json` in this directory
- Clone this repository `git clone https://github.com/tgrants/grade-check.git`
- Set environment variables
	- Copy template `cp .env.example .env`
	- Edit it `nano .env`
		- if `DJANGO_SECRET_KEY` is left empty, it will be generated when the app is run for the first time

### Development

- Create a virtual environment `python -m venv venv`
- Activate the virtual environment `source venv/bin/activate`
- Install requirements `pip install -r requirements.txt`
- Create superuser `python manage.py createsuperuser`
- Run development server `python manage.py runserver`

### Production (Docker on Debian 12)

- Install requirements
	- Git `sudo apt install git`
	- [Docker](https://docs.docker.com/engine/install/debian/)
		- Get docker compose `sudo apt install docker-compose`
		- Enable docker `sudo systemctl enable docker`
		- Start docker `sudo systemctl start docker`
		- Add user to docker group `sudo usermod -aG docker $USER`
- Build and start container `docker-compose up --build`
	- Add `-d` flag to run in background
- Open container shell `docker exec -it <web container> sh`
	- Apply migrations `python manage.py migrate`
	- Create super user `python manage.py createsuperuser`

## Contributing

Contributions are welcome.
For more information see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the terms of the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
See the [LICENSE](LICENSE) file for more information.
