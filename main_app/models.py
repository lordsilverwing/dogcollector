from django.db import models

from django.urls import reverse

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})
