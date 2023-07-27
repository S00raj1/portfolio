from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    email = models.CharField(max_length=120, null=False, blank=False)
    message = models.TextField(null=False, blank=False)


    def __str__(self):
        return self.name