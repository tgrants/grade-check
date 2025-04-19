from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .utils import get_student_scores


@login_required
def student_scores_view(request):
	username = request.user.username
	scores = get_student_scores(username)

	if scores is None:
		return render(request, 'core/home.html', {
			'error': 'No scores found or something went wrong.'
		})

	return render(request, 'core/home.html', {
		'scores': scores
	})
