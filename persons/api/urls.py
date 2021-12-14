from django.urls import path, include
# from rest_framework.templatetags import rest_framework
from django_filters import rest_framework

from . import views

app_name = 'persons'

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    # professor
    path('professor-list/', views.professor_list, name='s_professor_list'),
    path('professor-detail/<int:pk>', views.professor_detail, name='s_professor_detail'),

    # student
    path('student/list/', views.ListStudent_api.as_view(), name='s_student_list'),
    path('student/create', EmployeeCreateApi.as_view(), name='s_student_create'),
    path('student/update/<int:pk>', EmployeeUpdateApi.as_view(), name='s_student_update'),
    path('student/destroy/<int:pk>', EmployeeDestroyApi.as_view(), name='s_student_destroy'),

    path('student-list/', views.student_list, name='s_student_list'),
    path('student-detail/<int:pk>', views.student_detail, name='s_student_detail'),
    path('student-select-class/<int:pk>', views.SelectClassLessonAPI.as_view(), name='api_select_class_lesson'),

    # classLesson
    path('classLesson-list/', views.classLesson_list, name='s_classLesson_list'),
    path('student-detail/<int:pk>', views.classLesson_detail, name='s_classLesson_detail'),
]
