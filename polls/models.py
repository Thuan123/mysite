from __future__ import unicode_literals

from django.db import models
from time import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.template.defaultfilters import default
from django.db.models.deletion import CASCADE

# Create your models here.
"""class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text"""
        
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name        

class Question(models.Model):
    content = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.content
    
class Answer(models.Model):
    content = models.CharField(max_length=255)
    correct = models.BooleanField(default = None)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return self.content

class Exam(models.Model):
    time = models.IntegerField(default=0)
    start_time = models.DateTimeField('date published')
    mark = models.IntegerField(default=0)
    status = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.mark
        
class Result(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    def __str__(self):
        return self.question



        