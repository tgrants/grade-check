from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sheets.utils import get_student_scores


@login_required
def home(request):
	scores = None
	error = None

	if request.user.is_authenticated:
		scores = get_student_scores(request.user.username)
		if scores is None:
			error = "No scores found or something went wrong."

	return render(request, 'home.html', {'scores': scores, 'error': error})
