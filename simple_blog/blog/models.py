from django.db import models
from django.contrib.auth.models import User as Backend_user

# Create your models here.
class User(models.Model):
	registration_date = models.DateTimeField('date registrated')
	biogram = models.CharField(max_length=2000)
	credentials = models.ForeignKey(Backend_user,on_delete=models.CASCADE, default=None)
	def snippet(self):
		text = self.credentials.username + '  ' + self.biogram[0:10] + '...'
		return text
	def __str__(self):
		return self.credentials.username

class Thread(models.Model):
	title = models.CharField(max_length=50)
	def snippet(self):
		return title
	def __str__(self):
		return self.title
	def total_posts(self):
		posts = Post.objects.all().filter(thread__id=self.id)
		return len(posts)
		pass #TODO return the number of post in this thread 

class Post(models.Model):
	title = models.CharField(max_length= 100)
	content = models.TextField(max_length=5000)
	author = models.ForeignKey(User, on_delete= models.DO_NOTHING)
	thread = models.ForeignKey(Thread, on_delete=models.DO_NOTHING, default=None)
	def __str__(self):
		return self.title
	def snippet(self):
		if(len(self.content) > 30):
			return self.content[0:30] + "..."
		return self.content +  "..."

class Comment(models.Model):
	comment_text = models.CharField(max_length=2500)
	author = models.ForeignKey(User, on_delete= models.DO_NOTHING)
	post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)


		