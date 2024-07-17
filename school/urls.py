from django.urls import path
from .views import *

urlpatterns = [
    path('school', SchoolListView.as_view(), name='school-list'),
    path('school/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    path('school/create/', SchoolCreateView.as_view(), name='school-create'),
    path('school/<int:pk>/update/', SchoolUpdateView.as_view(), name='school-update'),
    path('school/<int:pk>/delete/', SchoolDeleteView.as_view(), name='school-delete'),
    path('classroom', ClassroomListView.as_view(), name='classroom-list'),
    path('classroom/<int:pk>/', ClassroomDetailView.as_view(), name='classroom-detail'),
    path('classroom/create/', ClassroomCreateView.as_view(), name='classroom-create'),
    path('classroom/<int:pk>/update/', ClassroomUpdateView.as_view(), name='classroom-update'),
    path('classroom/<int:pk>/delete/', ClassroomDeleteView.as_view(), name='classroom-delete')
]