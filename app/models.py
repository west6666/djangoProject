from django.db import models

class Team(models.Model):
    photo = models.ImageField(upload_to='products/%Y/%m/%d/')
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)

    def str(self):
        return self.name

class Pro(models.Model):
    photo = models.ImageField(upload_to='products/%Y/%m/%d/')
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    text = models.CharField(max_length=100)

    def str(self):
        return self.name


