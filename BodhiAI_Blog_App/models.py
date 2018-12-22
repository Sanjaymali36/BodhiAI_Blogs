from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import Truncator
import datetime

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='topics')
    Publisher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='topics')

    def __str__(self):
        return self.subject


class Blog(models.Model):
    Blog_Text = models.TextField(max_length=4000)
    title = models.CharField(max_length=200,blank=True)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE, related_name='posts')
    #created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts',null=True,default="BodhiAI")
    #updated_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='+')
    link1 = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)
    link3 = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.Blog_Text

class Comment(models.Model):

    user= models.ForeignKey(User,on_delete=models.CASCADE)

    comment= models.CharField(max_length=140, null=False)

    updated= models.DateTimeField(auto_now=True)

    timestamp= models.DateTimeField(auto_now_add=True)
    def _str__(self):
        return str(self.comment)




