from django.db import models

class Accountability(models.Model):
    date = models.DateTimeField()
    alert = models.PositiveSmallIntegerField()
    