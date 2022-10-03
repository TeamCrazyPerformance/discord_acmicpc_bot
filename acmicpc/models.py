from django.db import models

# Create your models here.
class Member(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    solved = models.IntegerField()