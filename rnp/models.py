from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    phone = models.CharField(unique=True, max_length=15)
    nationality = models.CharField(max_length=30)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
