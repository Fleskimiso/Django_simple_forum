from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.forum, name="forum"),
	path('register/',views.register, name='register'),
	path('login/', views.login, name='login'),
	path('logout/',views.logout,name='logout'),
	path('thread/<str:title>/',views.thread,name='thread'),
	path('thread/<str:title>/create_post/',views.create_post,name='create_post'),
	path('thread/posts/<int:identification>/', views.forum_post, name='post' ),
	path('thread/posts/comment',views.create_comment , name='create_comment' ),
	path('thread/posts/<int:identification>/delete/',views.delete_post, name='post_delete')
]