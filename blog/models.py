from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from pickle import TRUE
# Create your models here.

class Post(models.Model):
    Sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length = 150)
    slug = models.CharField(max_length=140)
    timeStamp = models.DateTimeField(default=now)
    content = models.TextField()


    def __str__(self):
        return "posted by " + self.author + ' - ' + self.title
    

class BlogComments(models.Model):
    Sno  = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    parent = models.ForeignKey('self',on_delete = models.CASCADE, null  =True)
    timestamp = models.DateTimeField(default=now)




    
