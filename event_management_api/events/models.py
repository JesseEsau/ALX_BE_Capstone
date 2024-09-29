from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True)
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=250)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    

    