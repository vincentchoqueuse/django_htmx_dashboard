from django.urls import path
from .views import *

urlpatterns = [
    path('student', StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student/create/', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('teacher', TeacherListView.as_view(), name='teacher-list'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher-create'),
    path('teacher/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher-update'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),
    path('employee', EmployeeListView.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete')
]