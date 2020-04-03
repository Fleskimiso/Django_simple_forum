from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, UserManager
from django.contrib.auth import authenticate, login as LOGIN, logout as LOGOUT
from django.core.exceptions import ObjectDoesNotExist

from .models import Thread, User as Forum_user , Post, Comment
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
	comments = Comment.objects.filter(post = post)
	print(comments)
	return render(request,'blog/post.html',{"post" : post , "comments": comments})

def delete_post(request,identification):
	post = Post.objects.get(pk = request.POST['post_id'])
	post_thread = post.thread.title
	Post.objects.remove(post)
	return redirect('blog:thread', post_thread);
def create_post(request,title):
		if request.method == 'GET':
			return render(request,'blog/create_post_template.html', {'title' : title})
		elif request.method == 'POST':
			title_post = request.POST['title_post']
			content = request.POST['content']
			author = Forum_user.objects.get(credentials = request.user)
			thread = Thread.objects.get(title=title)
			new_post = Post(title =title_post, content = content, author = author, thread=thread);
			new_post.save() #to do tests
			return redirect('blog:thread',title);

def create_comment(request): #TOBE TESTED 
	if request.method == 'POST':
		if request.user.is_authenticated == True:
			post_id = request.POST['post_id']
			comment_content = request.POST['content']
			user = Forum_user.objects.get(credentials__id = request.user.id)
			post_instance = Post.objects.get(pk=post_id)
			comment = Comment(comment_text=comment_content,author=user,post=post_instance)
			comment.save()
			return redirect('blog:post', post_id)
	elif request.method == 'GET':
		return redirect('blog:forum')
