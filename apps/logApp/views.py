from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import User

def index(request):
	if 'user' in request.session:
		return redirect('/success')
	else:
		return render (request, 'logApp/index.html')

def new(request):
	if request.method == "POST":
		errors = User.objects.reg_val(request.POST)
		if len(errors):
			print errors
			for tag, error in errors.iteritems():
				messages.error(request,error,extra_tags=tag)
				return redirect('/')
		else:
			request.session['user'] = User.objects.last().id
			return redirect('/success')
def success(request):
	if 'user' in request.session:
		return render(request, 'logApp/sucess.html' , {"User" : User.objects.get(id=request.session['user'])})
	else:
		return redirect ('/')

def signin(request):
	if request.method== "POST":
		errors = User.objects.log_val(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request,error,extra_tags=tag)
				return redirect('/')
		else:
			request.session['user'] = User.objects.get(email=request.POST['email']).id
			return redirect('/success')

def logout(request):
	request.session.pop('user')
	return redirect ('/')

# Create your views here.
