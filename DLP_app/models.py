from django.db import models
# Create your models here.

class Message(models.Model):
    content = models.TextField()
    pattern = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.content}"
    
class Pattern(models.Model):
    pattern = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.pattern}"
