from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # A short string field
    pub_date = models.DateTimeField("date published")  # A datetime field
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 
    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Foreign key to Question
    choice_text = models.CharField(max_length=200)  # A short string field
    votes = models.IntegerField(default=0)  # Integer field with default value 0
    def __str__(self):
        return self.choice_text