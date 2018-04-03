from django.db import models

class Message(models.Model):
    id = models.IntegerField(primary_key=True, )
    check = models.BooleanField(default=0)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)