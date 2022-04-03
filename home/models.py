from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    

class ProgressTree(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=1)
    level = models.IntegerField(default=1)
    
    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.id)


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=1)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    task_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class UserTree(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, default='changman')
    treelevel = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)