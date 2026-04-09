from django.db import models

class Contact(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    category = models.CharField(max_length=50, default="General")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
