import datetime

from django.db import models
from django.utils import timezone




# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    # ForeignKey to Choice model
    # choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='choices')
    

    def __str__(self):                
          return self.question_text
                                         
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    # ForeignKey to Question model
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
