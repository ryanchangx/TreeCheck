from django.db import models
from django.contrib.auth.models import User


class ProgressTree(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
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