from django.db import models

# Create your models here.
class Entry(models.Model):
    MOOD_CHOICES = [
        ('happy', '😊'),
        ('sad', '😢'),
        ('excited', '🤩'),
        ('anxious', '😰'),
        ('calm', '😌'),
        ('neutral', '😐'),
    ]
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, blank=True)
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    weather_icon = models.CharField(max_length=100, blank=True, null=True)
    temperature = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.content[:50] 