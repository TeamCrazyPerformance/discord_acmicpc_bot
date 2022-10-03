from django.db import models

# Create your models here.
class Member(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    solved = models.IntegerField()


class Submit(models.Model):
    submit_id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=20)
    problem_id = models.IntegerField()
    result = models.CharField(max_length=100)
