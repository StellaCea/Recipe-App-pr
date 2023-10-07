from django.db import models

class User(models.Model):
    username = models.CharField(max_length=120, unique=True)
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    bio = models.TextField()
    email = models.EmailField(null= True, blank=True, max_length=120)

    def __str__(self):
        return str(self.username)
