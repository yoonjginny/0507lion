# todo/models.py

from django.db import models
from datetime import datetime

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date= models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
        
from django.contrib import admin
admin.site.register(Todo)
