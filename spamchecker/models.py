from django.db import models

# Create your models here.

class Sms(models.Model):
    content = models.CharField(max_length=200)
    spamProbability = models.FloatField()

    def __str__(self):
        return self.question_text