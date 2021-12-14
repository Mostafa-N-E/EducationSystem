from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('student/signup/', views.Signup_STU.as_view(), name='signup_student'),
    path('staff/signup/', views.Signup_STF.as_view(), name='signup_staff'),
    path('professor-profile/<int:pk>', views.Profile_P.as_view(), name='professor_profile'),
    path('student-profile/<int:pk>', views.Profile_STU.as_view(), name='student_profile'),
    path('staff-profile/<int:pk>', views.Profile_STF.as_view(), name='staff_profile'),

]
