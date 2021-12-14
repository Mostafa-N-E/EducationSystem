from django.shortcuts import render, redirect
from .forms import SignUp_STU_Form,SignUp_STF_Form,StudentForm
from django.views.generic import UpdateView, CreateView
from persons.models import Student,Professor,UniversityStaff,UnivercityPersident
from django.contrib.auth import views as auth_views, forms
from django.shortcuts import resolve_url

class Signup_STU(CreateView):
    form_class = SignUp_STU_Form
    template_name = 'accounts/signup.html'
    success_url = '/accounts/login'


class Signup_STF(CreateView):
    form_class = SignUp_STF_Form
    template_name = 'accounts/signup.html'
    success_url = '/accounts/login'

presidents =  [president.username for president in list(UnivercityPersident.objects.all())]
staffs =  [staff.username for staff in list(UniversityStaff.objects.all())]
professors = [professor.username for professor in list(Professor.objects.all())]
students = [student.username for student in list(Student.objects.all())]
class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        if self.request.user.username in professors:
            return resolve_url('persons:show_classes_by_Professor')
        elif self.request.user.username in students:
            return resolve_url('persons:STU_show_classes')
        elif self.request.user.username in staffs:
            return resolve_url('persons:show_classes_by_staff')
        elif self.request.user.username in presidents:
            return resolve_url('persons:show_classes_by_president')


class Profile_STU(UpdateView):
    model = Student
    fields = ['username', 'first_name', 'last_name', 'phone_number', 'email',]
    # form_class = StudentForm
    template_name = 'accounts/student_profile.html'
    success_url = '/persons/student/class/'


class Profile_P(UpdateView):
    model = Professor
    fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', ]
    template_name = 'accounts/professor_profile.html'
    success_url = 'persons/professor/class/'


class Profile_STF(UpdateView):
    model = UniversityStaff
    fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', ]
    template_name = 'accounts/staff_profile.html'
    success_url = 'persons/staff/class/'


class Profile_PRS(UpdateView):
    model = UnivercityPersident
    fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', ]
    template_name = 'accounts/professor_profile.html'
    success_url = 'persons/president/class/'



