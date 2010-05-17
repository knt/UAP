from django.db import models
from django.contrib.auth.models import User




class ClaimedLink(models.Model):
    concept1 = models.CharField(max_length=50)
    concept2 = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)
    used = models.IntegerField(default=0)
    userid = models.ForeignKey(User)



class GameProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    points = models.IntegerField(default=0)




User.profile = property(lambda u: GameProfile.objects.get_or_create(user=u)[0])    

    
