from generic.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, CustomDeleteView
from .models import Teacher, Student, Employee
from .filters import TeacherFilter, StudentFilter, EmployeeFilter


class StudentListView(CustomListView):
    model = Student
    filter_class = StudentFilter

class StudentCreateView(CustomCreateView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'classroom']

class StudentDetailView(CustomDetailView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'classroom']

class StudentUpdateView(CustomUpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'classroom']

class StudentDeleteView(CustomDeleteView):
    model = Student


class TeacherListView(CustomListView):
    model = Teacher
    filter_class = TeacherFilter

class TeacherCreateView(CustomCreateView):
    model = Teacher
    fields = ['first_name', 'last_name', 'email', 'classroom']

class TeacherDetailView(CustomDetailView):
    model = Teacher
    fields = ['first_name', 'last_name', 'email', 'classroom']

class TeacherUpdateView(CustomUpdateView):
    model = Teacher
    fields = ['first_name', 'last_name', 'email', 'classroom']

class TeacherDeleteView(CustomDeleteView):
    model = Teacher


class EmployeeListView(CustomListView):
    model = Employee
    filter_class = EmployeeFilter

class EmployeeCreateView(CustomCreateView):
    model = Employee
    fields = ['first_name', 'last_name', 'email', 'school']

class EmployeeDetailView(CustomDetailView):
    model = Employee
    fields = ['first_name', 'last_name', 'email', 'school']

class EmployeeUpdateView(CustomUpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'email', 'school']

class EmployeeDeleteView(CustomDeleteView):
    model = Employee

