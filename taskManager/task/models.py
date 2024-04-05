from django.db import models
import random
import string

def randomid():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(9))

class user(models.Model):
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    contact=models.CharField(max_length=100)
    id= randomid()

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    usserAssigned = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.title