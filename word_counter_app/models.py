from django.db import models
from django.utils import timezone

# Create your models here.


class T1(models.Model):
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.id} ,{self.date}'


class T2(models.Model):
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.id} ,{self.date}'


class QC(models.Model):
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.id} ,{self.date}'
