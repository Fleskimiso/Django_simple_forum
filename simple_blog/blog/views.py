from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, UserManager
from django.contrib.auth import authenticate, login as LOGIN, logout as LOGOUT
from django.core.exceptions import ObjectDoesNotExist

from .models import Thread, User as Forum_user , Post
import datetime
# Create your views here.
def forum(request):

	threads = Thread.objects.all()
	return render(request, 'blog/index.html',{"threads": threads}) #our future main page


def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		try:
			u = User.objects.get(username=username)
			return render(request,'blog/register_page.html',{"warning": "There is already someone with this name"})
		except ObjectDoesNotExist as exep:
			#usermanager = UserManager()
			user = User.objects.create_user(username=username, password=password)
			user.save()
			f_user = Forum_user(biogram="nothing too fancy", registration_date =datetime.date.today(),
				credentials=user)
			f_user.save()
			LOGIN(request, user)
			return redirect('blog:forum')

	return render(request,'blog/register_page.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		LOGIN(request,user)
		return redirect('blog:forum')
	return render(request,'blog/login_page.html')

def logout(request):
	LOGOUT(request)
	return redirect('blog:login')

def thread(request,title):
	thread = Thread.objects.all().get(title=title)
	posts = Post.objects.filter(thread=thread)
	return render(request,'blog/thread.html', {'title': thread.title, 'posts': posts})

def forum_post(request,identification):
	post = Post.objects.get(pk=identification)
	return render(request,'blog/post.html',{"post" : post })