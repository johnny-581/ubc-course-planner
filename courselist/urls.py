from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mycourses/', views.CoursesByUserListView.as_view(), name='my_courses'),
]
