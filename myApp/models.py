from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()

    def __str__(self):
        return f"{self.name}"