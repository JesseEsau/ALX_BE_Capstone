from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True)
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=250)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def is_full(self):
        return self.registrations.count() >= self.capacity

    def __str__(self):
        return self.title

class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    tiemstamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'event']
    
    def __str__(self):
        return f"{self.user.username} has registered for {self.event.title}"

    

    

    