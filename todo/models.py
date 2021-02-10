from django.db import models
from accounts.models import User

# Create your models here.


class ToDo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    importance = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    complete_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
