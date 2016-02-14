from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from users.models import UserProfile


def index(request):
	"""Direct Users to home page when first accessing site"""
	return render(request, 'index.html')

def auth_login(request):
	"""Allow users to log in"""
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/blog')
		else:
			print("Invalid Credentials")
	return render(request, 'users/login.html')

	