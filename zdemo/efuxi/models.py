from django.db import models

# Create your models here.


class Stu(models.Model):
    name = models.CharField(max_length=20,null=True)
    age = models.IntegerField()
    gender = models.BooleanField(default=False)

