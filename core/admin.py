from django.contrib import admin
from django.urls import path
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_str

class BulkUserUploadForm(forms.Form):
	data = forms.CharField(
		widget=forms.Textarea(attrs={"rows": 10, "cols": 80}),
		help_text="Paste users in the format: username,password"
	)

admin.site.unregister(User)

class CustomUserAdmin(admin.ModelAdmin):
	change_list_template = "admin/bulk_user_changelist.html"

	def get_urls(self):
		urls = super().get_urls()
		custom_urls = [
			path('bulk-upload/', self.admin_site.admin_view(self.bulk_upload_view), name='bulk-user-upload'),
		]
		return custom_urls + urls

	def bulk_upload_view(self, request):
		if request.method == 'POST':
			form = BulkUserUploadForm(request.POST)
			if form.is_valid():
				created_users = []
				raw_data = form.cleaned_data['data']
				lines = raw_data.strip().split('\n')
				created_count = 0
				for line in lines:
					try:
						username, password = line.strip().split(',')
						if not User.objects.filter(username=username).exists():
							user = User.objects.create_user(username=username, password=password)
							created_users.append(user)
							created_count += 1
					except ValueError:
						messages.error(request, f"Invalid line: '{line}'")
				if created_users:
					LogEntry.objects.log_action(
						user_id=request.user.pk,
						content_type_id=ContentType.objects.get_for_model(User).pk,
						object_id=created_users[0].pk,  # Just reference one user
						object_repr=f"Bulk created {len(created_users)} users",
						action_flag=ADDITION,
						change_message=f"Bulk created users: {', '.join([u.username for u in created_users])}"
					)
				messages.success(request, f"Successfully created {created_count} users.")
				return redirect('..')
		else:
			form = BulkUserUploadForm()
		context = {
			'form': form,
			'title': 'Bulk Upload Users'
		}
		return render(request, 'admin/bulk_user_upload.html', context)

admin.site.register(User, CustomUserAdmin)
