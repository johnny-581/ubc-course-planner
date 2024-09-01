from django.db import models
from django.urls import reverse

class Course(models.Model):
    subject = models.CharField(max_length=100)
    code = models.SmallIntegerField()
