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

### Production (Docker on Debian 12)

- Install requirements
	- Git `sudo apt install git`
	- [Docker](https://docs.docker.com/engine/install/debian/)
		- Get docker compose `sudo apt install docker-compose`
		- Enable docker `sudo systemctl enable docker`
		- Start docker `sudo systemctl start docker`
		- Add user to docker group `sudo usermod -aG docker $USER`
- Clone the repository `git clone https://github.com/tgrants/grade-check.git`
- Download and place your `credentials.json` in this directory
- Set environment variables
	- Copy template `cp .env.example .env`
	- Edit it `nano .env`
		- if `DJANGO_SECRET_KEY` is left empty, it will get generated when the app is run for the first time
- Build and start container `docker-compose up --build`
	- Add `-d` flag to run in background
- Open container shell `docker exec -it <web container> sh`
	- Apply migrations `python manage.py migrate`
	- Create super user `python manage.py createsuperuser`

## Contributing

Contributions are welcome.
For more information see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

This project is licensed under the terms of the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
See the [LICENSE](LICENSE) file for more information.
