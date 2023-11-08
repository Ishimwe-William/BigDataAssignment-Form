from django.shortcuts import render, redirect, get_object_or_404

from rnp.models import Student
from rnp.studentForm import StudentForm


def index(request):
    return render(request, 'index.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'add_student.html', {'form': form})


def confirm_delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'confirm_delete_student.html', {'student': student})


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect('student_list')