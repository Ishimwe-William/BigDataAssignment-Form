from django.urls import path

from rnp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.student_list, name='student_list'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('confirm_delete_student/<int:student_id>/', views.confirm_delete_student, name='confirm_delete_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
]
