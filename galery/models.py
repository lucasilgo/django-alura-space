from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    caption = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    photo = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"Photo [name={self.name}]"
