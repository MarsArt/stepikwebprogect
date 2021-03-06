from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.IntegerField(default=0)




class Answer(models.Model):
    text=models.TextField()
    added_at =  models.DateField()
    question = models.TextField()
    author = models.ForeignKey(User)


