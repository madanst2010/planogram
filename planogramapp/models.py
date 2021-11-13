from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
# Create your models here.
import jsonfield

class User(AbstractUser):
    pass
class Planogram(models.Model):
    name = models.CharField(max_length=255)
class PlanogramDetails(models.Model):
    plano_id = models.ForeignKey(Planogram, on_delete=CASCADE)
    cat_name = models.CharField(max_length=255)
    cat_color = models.CharField(max_length=255)
    data_point = models.JSONField()
