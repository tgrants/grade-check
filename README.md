# GradeCheck

This app allows educators to share scores from a Google spreadsheet without giving students direct access to it.

> [!WARNING]
>
> This project is in the early stages of development. Breaking changes may occur.

## Features

<!-- Commented features are planned-->
<!--
- Groups and permissions - mutiple sheets, educators and classes can be added.
- Multi-language support - currently supports English and Latvian. Administrators can set the default and available languages.
- Accessibility - 100% accessibility score on [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview). Tested with a screen reader.
- Maintainability - easy to update to a newer version.
-->

## Setup

Quick setup instructions for Linux.
For more detailed instructions, see the [documentation](docs/).

- Prepare [Google sheets](https://workspace.google.com/products/sheets/)
	- Create a project in [Google Cloud console](https://console.cloud.google.com)
		- Enable Google Sheets API
		- Create a service account
		- Download and place your `credentials.json` in this directory
	- Create your sheet (see [docs/sheet-format.md](docs/sheet-format.md))
		- Share it with the service account
- Clone this repository `git clone https://github.com/tgrants/grade-check.git`
- Set environment variables
	- Copy template `cp .env.example .env`
	- Edit it `nano .env`
		- if `DJANGO_SECRET_KEY` is left empty, it will be generated when the app is run for the first time
- Install [Docker](https://docs.docker.com/engine/install/debian/)
	- Get docker compose `sudo apt install docker-compose`
	- Enable docker `sudo systemctl enable docker`
	- Start docker `sudo systemctl start docker`
	- Add user to docker group `sudo usermod -aG docker $USER`
- Build and start container
	- Development: `docker-compose -f docker-compose.dev.yml up --build`
	- Production: `docker-compose up --build`
		- Add `-d` flag to run in background

## Updating

> [!WARNING]
>
> Migrating your data to a new version is currently not supported, but will be in the future.

- Read the [changelogs](https://github.com/tgrants/grade-check/releases)
- Pull the latest changes `git pull`
- Make sure `.env` has the same values as `.env.example`
- Rebuild the containers

## Contributing

Contributions are welcome.
For more information see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the terms of the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
See the [LICENSE](LICENSE) file for more information.
