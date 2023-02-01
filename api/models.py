from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.body}"


