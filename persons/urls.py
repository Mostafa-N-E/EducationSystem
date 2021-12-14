from django.urls import path
from . import views

app_name = 'persons'

urlpatterns = [

    # student
    path('student/class/', views.ClassShow.as_view(), name='STU_show_classes'),
    path('student/class-detail/<int:pk>', views.ClassDetail.as_view(), name='STU_class_detail'),
    path('student/select-classes/', views.SelectClass.as_view(), name='STU_select_classes'),
    path('student/select-class/<int:pk>', views.SelectClassLesson, name='STU_select_class'),
    path('student/rented-book/', views.RentedBook.as_view(), name='STU_show_rented_book'),

    # staff
    path('staff/class/', views.ClassShow_by_STF_PRS.as_view(), name='show_classes_by_staff'),
    path('staff/profssors/', views.ProfssorShow_by_STF_PRS.as_view(), name='show_profssors_by_staff'),
    path('staff/students/', views.StudentShow_by_STF_PRS.as_view(), name='show_students_by_staff'),
    path('staff/delete-student/<int:stu_pk>/<int:class_pk>', views.delete_stu_by_staff_and_persident, name='delete_student_by_staff'),
    path('staff/student_select_class/<pk>', views.SelectClass_by_STF_PRS.as_view(), name='SelectClasses_by_staff'),
    path('staff/select-class/<int:stu_pk>/<int:class_pk>', views.SelectClassLesson_by_STF_PRS,name='SelectClass_by_staff'),

    # professor
    path('professor/class/', views.P_ClassShow.as_view(), name='show_classes_by_Professor'),
    path('professor/students/', views.P_StudentShow.as_view(), name='show_students_by_Professor'),
    path('professor/delete-student/<int:stu_pk>/<int:class_pk>', views.delete_stu_by_professor, name='delete_student_by_Professor'),
    path('professor/student_select_class/<pk>', views.SelectClass_by_P.as_view(), name='SelectClasses_by_Professor'),
    path('professor/select-class/<int:stu_pk>/<int:class_pk>', views.SelectClassLesson_by_P, name='SelectClass_by_Professor'),

    # persident
    path('persident/class/', views.ClassShow_by_STF_PRS.as_view(), name='show_classes_by_persident'),
    path('persident/students/', views.StudentShow_by_STF_PRS.as_view(), name='show_students_by_persident'),
    path('persident/delete-student/<int:stu_pk>/<int:class_pk>', views.delete_stu_by_staff_and_persident, name='delete_student_by_persident'),
    path('persident/student_select_class/<pk>', views.SelectClass_by_STF_PRS.as_view(), name='SelectClasses_by_persident'),
    path('persident/select-class/<int:stu_pk>/<int:class_pk>', views.SelectClassLesson_by_STF_PRS,name='SelectClass_by_persident'),

]
