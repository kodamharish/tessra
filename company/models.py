from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.IntegerField()
    subject = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return str(self.id)