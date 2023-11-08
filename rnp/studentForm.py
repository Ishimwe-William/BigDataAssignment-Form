from django import forms
from rnp.models import Student


class StudentForm(forms.ModelForm):
    # Define a form class that inherits from Django's ModelForm

    class Meta:
        model = Student
        # Specify the model that this form is based on (the 'Student' model)

        fields = '__all__'
        # Include all fields from the model in the form
