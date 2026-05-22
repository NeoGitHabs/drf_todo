from django.db import models
from django.db.models import CASCADE

class Type(models.Model):
    status = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.status

class Todo(models.Model):
    Type_connect_with_Todo = models.ForeignKey(Type, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
