from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView
from .models import *
from .models import ClassLesson
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.
from django.contrib.auth.models import Permission
from .utils import create_PDF
per = Permission.objects.all()
dd = per.filter(name='Can view content type').first()
print(dd.name)


import logging
logger = logging.getLogger('root')
#------------------------------------------------------ STUDENT -------------------------------------------------------
class ClassShow(LoginRequiredMixin,generic.ListView):
    model = ClassLesson
    template_name = 'student/home.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return ClassLesson.objects.all()
        else:
            return ClassLesson.objects.filter(students__username=self.request.user.username)


class ClassDetail(LoginRequiredMixin,generic.DetailView):
    model = ClassLesson
    template_name = 'student/class_detail.html'
    context_object_name = "classLesson"


class SelectClass(LoginRequiredMixin,generic.ListView):
    model = ClassLesson

    def get(self, request, *args, **kwargs):
        stu = Student.objects.filter(username=self.request.user.username).first()
        have_lesson = ClassLesson.objects.filter(students__username=self.request.user.username).filter(cluss__college__name=stu.college.name)
        have_not_lesson = ClassLesson.objects.exclude(students__username=self.request.user.username).filter(cluss__college__name=stu.college.name)
        context = {'have_lesson': have_lesson, "have_not_lesson": have_not_lesson}
        return render(request, 'student/select_class.html', context)


def export_PDF(request,pk):
    stu = Student.objects.filter(id=pk).first()
    have_lesson = ClassLesson.objects.filter(students__username=stu.user.username).filter(cluss__college__name=stu.college.name)
    subject = f'report card {stu.user.username}'
    create_PDF(subject,have_lesson)
    return JsonResponse({ 'status': 1,})

def SelectClassLesson(request,pk):
    classLesson = ClassLesson.objects.get(pk = pk)
    students = list(classLesson.students.all())
    students_username = [student.username for student in students]
    if request.user.username in students_username:
        new_stu = Student.objects.filter(username=request.user.username).first()
        classLesson.students.remove(new_stu)
        classLesson.save()
        return JsonResponse({ 'status': 1,})
    else:
        new_stu = Student.objects.filter(username=request.user.username).first()
        classLesson.students.add(new_stu)
        classLesson.save()
        return JsonResponse({'status': 2, })

class RentedBook(LoginRequiredMixin,generic.ListView):
    model = Student
    template_name = 'student/books_rent.html'
    def get_queryset(self):
        return Student.objects.filter(username=self.request.user.username)


#------------------------------------------------------ PROFESSOR -----------------------------------------------------
class P_ClassShow(LoginRequiredMixin,generic.ListView):
    model = ClassLesson
    # permission_required = (dd.name,)PermissionRequiredMixin
    template_name = 'professer/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ClassLesson.objects.all()
        else:
            return ClassLesson.objects.filter(professor__username=self.request.user.username)


class P_StudentShow(LoginRequiredMixin,generic.ListView):
    model = ClassLesson
    template_name = 'professer/student_show.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ClassLesson.objects.all()
        else:
            return ClassLesson.objects.filter(professor__username=self.request.user.username).annotate(Count('students'))


def delete_stu_by_professor(request,stu_pk,class_pk):   #??????
    class_lesson = ClassLesson.objects.filter(id=stu_pk).first()
    student = Student.objects.filter(id=class_pk).first()
    class_lesson.students.remove(student)
    class_lesson.save()
    return HttpResponse('success')

class SelectClass_by_P(LoginRequiredMixin,ListView):

    model = ClassLesson
    template_name = 'professer/student_select_class_by_P.html'

    # def get(self, request):
    #     pk = int(self.kwargs['pk'])
    #     student = Student.objects.filter(id=pk).first()
    #     have_lesson = ClassLesson.objects.filter(students__username=student.username)
    #     have_not_lesson = ClassLesson.objects.exclude(students__username=student.username)
    #     context = {'have_lesson': have_lesson, "have_not_lesson": have_not_lesson}
    #     return render(request, 'professer/student_select_class_by_P.html', context)
    def get_context_data(self, **kwargs):
        pk = int(self.kwargs['pk'])
        student = Student.objects.filter(id=pk).first()
        have_lesson = ClassLesson.objects.filter(students__username=student.username).filter(cluss__college__name=student.college.name)
        have_not_lesson = ClassLesson.objects.exclude(students__username=student.username).filter(cluss__college__name=student.college.name)
        context = {'have_lesson': have_lesson, "have_not_lesson": have_not_lesson, "student":student}
        return context

def SelectClassLesson_by_P(request,stu_pk,class_pk):
    class_lesson = ClassLesson.objects.filter(id=class_pk).first()
    student = Student.objects.filter(id=stu_pk).first()
    students = list(class_lesson.students.all())
    students_username = [student.username for student in students]
    if student.username in students_username:
        class_lesson.students.remove(student.id)
        class_lesson.save()
        return JsonResponse({ 'status': 1,})
    else:
        class_lesson.students.add(student.id)
        class_lesson.save()
        return JsonResponse({'status': 2, })
#------------------------------------------------ STAFF & PERSIDENT -------------------------------------------------------
class ClassShow_by_STF_PRS(LoginRequiredMixin,generic.ListView):
    model = ClassLesson
    template_name = 'staff/home.html'

    def get_queryset(self):
        return ClassLesson.objects.all()


class ProfssorShow_by_STF_PRS(LoginRequiredMixin,generic.ListView):
    model = ClassLesson
    template_name = 'staff/professor_show.html'

    def get_queryset(self):
        return ClassLesson.objects.all()


class StudentShow_by_STF_PRS(LoginRequiredMixin,generic.ListView):
    model = ClassLesson
    template_name = 'staff/student_show.html'

    def get_queryset(self):
        return ClassLesson.objects.all().annotate(Count('students'))


def delete_stu_by_staff_and_persident(request,stu_pk,class_pk):   #??????
    class_lesson = ClassLesson.objects.filter(id=stu_pk).first()
    student = Student.objects.filter(id=class_pk).first()
    class_lesson.students.remove(student)
    class_lesson.save()
    return HttpResponse('success')

class SelectClass_by_STF_PRS(LoginRequiredMixin,ListView):

    model = ClassLesson
    template_name = 'professer/student_select_class_by_P.html'

    # def get(self, request):
    #     pk = int(self.kwargs['pk'])
    #     student = Student.objects.filter(id=pk).first()
    #     have_lesson = ClassLesson.objects.filter(students__username=student.username)
    #     have_not_lesson = ClassLesson.objects.exclude(students__username=student.username)
    #     context = {'have_lesson': have_lesson, "have_not_lesson": have_not_lesson}
    #     return render(request, 'professer/student_select_class_by_P.html', context)
    def get_context_data(self, **kwargs):
        pk = int(self.kwargs['pk'])
        student = Student.objects.filter(id=pk).first()
        have_lesson = ClassLesson.objects.filter(students__username=student.username)
        have_not_lesson = ClassLesson.objects.exclude(students__username=student.username)
        context = {'have_lesson': have_lesson, "have_not_lesson": have_not_lesson, "student":student}
        return context

def SelectClassLesson_by_STF_PRS(request,stu_pk,class_pk):
    class_lesson = ClassLesson.objects.filter(id=class_pk).first()
    student = Student.objects.filter(id=stu_pk).first()
    students = list(class_lesson.students.all())
    students_username = [student.username for student in students]
    if student.username in students_username:
        class_lesson.students.remove(student.id)
        class_lesson.save()
        return JsonResponse({ 'status': 1,})
    else:
        class_lesson.students.add(student.id)
        class_lesson.save()
        return JsonResponse({'status': 2, })



#-------------------------------------------------------- PERSIDENT --------------------------------------------------


