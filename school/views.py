from generic.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, CustomDeleteView
from .models import School, Classroom
from .filters import SchoolFilter, ClassroomFilter


class SchoolListView(CustomListView):
    model = School
    filter_class = SchoolFilter

class SchoolCreateView(CustomCreateView):
    model = School
    fields = ['name', 'address']

class SchoolDetailView(CustomDetailView):
    model = School
    fields = ['name', 'address']

class SchoolUpdateView(CustomUpdateView):
    model = School
    fields = ['name', 'address']

class SchoolDeleteView(CustomDeleteView):
    model = School


class ClassroomListView(CustomListView):
    model = Classroom
    filter_class = ClassroomFilter

class ClassroomCreateView(CustomCreateView):
    model = Classroom
    fields = ['school', 'name', 'capacity']

class ClassroomDetailView(CustomDetailView):
    model = Classroom
    fields = ['school', 'name', 'capacity']

class ClassroomUpdateView(CustomUpdateView):
    model = Classroom
    fields = ['school', 'name', 'capacity']

class ClassroomDeleteView(CustomDeleteView):
    model = Classroom