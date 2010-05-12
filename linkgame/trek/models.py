from django.db import models
from django.contrib.auth.models import User




class ClaimedLink(models.Model):
    concept1 = models.CharField(max_length=50)
    concept2 = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)
    userid = models.ForeignKey(User)
