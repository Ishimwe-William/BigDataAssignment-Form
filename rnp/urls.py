from django.urls import path
from rnp import views

urlpatterns = [
    path('', views.index, name='index'),
    # Map the root URL to the 'index' view, assigning it the name 'index'

    path('students/', views.student_list, name='student_list'),
    # Map the 'students/' URL to the 'student_list' view, assigning it the name 'student_list'

    path('add_student/', views.add_student, name='add_student'),
    # Map the 'add_student/' URL to the 'add_student' view, assigning it the name 'add_student'

    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    # Map the 'edit_student/<int:student_id>/' URL to the 'edit_student' view, assigning it the name 'edit_student'

    path('confirm_delete_student/<int:student_id>/', views.confirm_delete_student, name='confirm_delete_student'),
    # Map the 'confirm_delete_student/<int:student_id>/' URL to the 'confirm_delete_student' view, assigning it the
    # name 'confirm_delete_student'

    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    # Map the 'delete_student/<int:student_id>/' URL to the 'delete_student' view, assigning it the name
    # 'delete_student'
]
