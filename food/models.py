from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


class Food(TimeStampedModel, models.Model):
    name = models.CharField(max_length=180)
    carbs = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
