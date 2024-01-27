from django.db import models


class User(models.Model):
    login = models.CharField(max_length=20)
    email = models.EmailField()
    role = models.CharField(max_length=2, choices={
        'AD': 'Admin',
        'US': 'User'
    })


