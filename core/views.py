from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from sheets.utils import get_student_scores

from .forms import UserProfileForm


@login_required
def home(request):
	scores = None
	error = None

	if request.user.is_authenticated:
		scores = get_student_scores(request.user.username)
		if scores is None:
			error = "No scores found or something went wrong."

	return render(request, 'home.html', {'scores': scores, 'error': error})


@login_required
def profile_view(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = UserProfileForm(instance=request.user)
	return render(request, 'profile.html', {'form': form})
