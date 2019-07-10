from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/projects')
    summary = models.CharField(max_length=200)
