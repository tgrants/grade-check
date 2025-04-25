from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
	help = 'Creates a default superuser'

	def handle(self, *args, **options):
		User = get_user_model()
		if User.objects.exists():
			self.stdout.write(self.style.WARNING('Users already exist - skipping default user creation'))
			return
		User.objects.create_superuser(
			username='admin',
			email='admin@email.invalid',
			password='gradecheck'
		)
		self.stdout.write(self.style.SUCCESS('Default superuser created'))
