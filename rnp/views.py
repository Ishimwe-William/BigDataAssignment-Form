from django.shortcuts import render, redirect, get_object_or_404
from rnp.models import Student
from rnp.studentForm import StudentForm


def index(request):
    # Render the 'index.html' template
    return render(request, 'index.html')


def student_list(request):
    # Retrieve all students from the database
    students = Student.objects.all()
    # Render the 'student_list.html' template, passing the students to the template
    return render(request, 'student_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = StudentForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the student record and redirect to the student list
            form.save()
            return redirect('student_list')
    else:
        # If the request method is not POST, display the form
        form = StudentForm()
    # Render the 'add_student.html' template, passing the form to the template
    return render(request, 'add_student.html', {'form': form})


def edit_student(request, student_id):
    # Get the student object with the given ID or return a 404 error if not found
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            # If the form is valid, save the updated student record and redirect to the student list
            form.save()
            return redirect('student_list')
    else:
        # If the request method is not POST, display the form with the current student's data
        form = StudentForm(instance=student)
    # Render the 'add_student.html' template, passing the form to the template
    return render(request, 'add_student.html', {'form': form})


def confirm_delete_student(request, student_id):
    # Get the student object with the given ID or return a 404 error if not found
    student = get_object_or_404(Student, pk=student_id)
    # Render the 'confirm_delete_student.html' template, passing the student to the template
    return render(request, 'confirm_delete_student.html', {'student': student})


def delete_student(request, student_id):
    # Get the student object with the given ID or return a 404 error if not found
    student = get_object_or_404(Student, pk=student_id)
    # Delete the selected student and redirect to the student list
    student.delete()
    return redirect('student_list')
