# models.py
from django.db import models

class Request(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Request {self.id} at {self.timestamp}'
