from django.db import models


class Student(models.Model):
    # Define a Django model named 'Student'

    name = models.CharField(max_length=50)
    # Create a field for the student's name (maximum length of 50 characters)

    dob = models.DateField()
    # Create a field for the student's date of birth

    phone = models.CharField(unique=True, max_length=15)
    # Create a field for the student's phone number (unique constraint, maximum length of 15 characters)

    nationality = models.CharField(max_length=30)
    # Create a field for the student's nationality (maximum length of 30 characters)

    createdAt = models.DateField(auto_now_add=True)

    # Create a field for the date the student record was created (auto-generated upon creation)

    def __str__(self):
        # Define a string representation for the model
        return self.name

# python manage.py makemigrations
# python manage.py migrate
