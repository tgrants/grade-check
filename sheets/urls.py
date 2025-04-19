from django.urls import path
from .views import student_scores_view

urlpatterns = [
	path('my-scores/', student_scores_view, name='student_scores'),
]
