"""
Management command to create a default Django superuser.

This command creates a superuser if none exist, using either provided command-line
arguments, environment variables, or fallback defaults. Intended for easy setup
in development or initial deployments.
"""

import os

from django.core.management import color_style
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
	"""
	Django management command to create a default superuser.

	Optional arguments:
	--username: specify the superuser username (default 'admin' or env var)
	--email: specify the superuser email address (default 'admin@email.invalid' or env var)
	--password: specify the superuser password (default 'gradecheck' or env var)

	If any user exists already, user creation will be skipped.
	"""

	help = 'Creates a default superuser'

	def add_arguments(self, parser):
		parser.add_argument(
			'--username',
			type = str,
			help = 'Specify the superuser username',
			default = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
		)
		parser.add_argument(
			'--email',
			type=str,
			help='Specify the superuser email',
			default=os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@email.invalid')
		)
		parser.add_argument(
			'--password',
			type=str,
			help='Specify the superuser password',
			default=os.getenv('DJANGO_SUPERUSER_PASSWORD', 'gradecheck')
		)

	def handle(self, *args, **options):
		user_model = get_user_model()
		style = color_style()

		if user_model.objects.exists():
			self.stdout.write(style.SUCCESS('Skipping default user creation')) # pylint: disable=no-member
			return

		username = options['username']
		email = options['email']
		password = options['password']

		try:
			user_model.objects.create_superuser(username=username, email=email, password=password)
			self.stdout.write(style.SUCCESS(f'Default superuser "{username}" created')) # pylint: disable=no-member
		except Exception as e:
			raise CommandError(f'Failed to create superuser: {e}') from e
