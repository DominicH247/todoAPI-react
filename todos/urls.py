from django.urls import path

from .views import ListTodo, DetailTodo

url_patterns = [
	
	path('<int:pk>/', DetailTodo.as_view()),
	path('', ListTodo.as_view()),

] 