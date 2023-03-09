from django.db import models

# Create your models here.

class Event(models.Model):
    events_image = models.ImageField(upload_to='event_images')
    events_text = models.CharField(max_length=300)