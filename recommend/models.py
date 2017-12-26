from django.db import models

class User(models.Model):
    count=models.IntegerField()

class snap(models.Model):
    name=models.CharField(max_length=100)
    file=models.FileField()

class logo(models.Model):
    file=models.FileField()

class movies(models.Model):
    name=models.CharField(max_length=100)
    url=models.CharField(max_length=150)
    modifiedname=models.CharField(max_length=150,default="default")
    movieid=models.IntegerField(default=0)


    def __str__(self):
        return self.name
# Create your models here.
