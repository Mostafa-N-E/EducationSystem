from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreateClassForm, Student
from .models import *
from persons.models import ClassLesson
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

#
# import json
#
# from django.contrib.auth.models import User
# from django.http import HttpResponse
# from django.shortcuts import render
#
#
# def SelectClassLesson(request):
#     # if request.is_ajax():
#     username = request.GET.get('user', '')
#     user = User.objects.get(username=username)
#
#     classLesson_id = request.GET.get('classLesson_id', '')
#     classLesson = ClassLesson.objects.get(pk=classLesson_id)
#     print(classLesson)
#     if request.user.username in classLesson.students:
#         classLesson.remove(student = request.user.username)
#         # return {'status': 1}
#     else:
#         classLesson.add(student = request.user.username)
#         # return {'status': 2}
#
#     json_response = {'classLesson': {'classLesson_id': classLesson_id}}
#
#     return HttpResponse(json.dumps(json_response),
#         content_type='application/json')
#
#     # return render(request, 'environment_education/select_class.html', {'user': ''})
#
#
#




class CreateClass( LoginRequiredMixin,CreateView):
    model = ClassLesson
    template_name = ""
    fields = ['name', 'status','college',]
def create_class(request):
    if request.POST:
        form = CreateClassForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('environment_education:class_detail')

        else:
            return render(request, 'environment_education/create_class_form.html', {"create_class_form": form})

    form = CreateClassForm()
    return render(request, 'environment_education/create_class_form.html', {"create_class_form": form})

#
# def create_classLesson(request):
#     class_lesson = ClassLesson.objects.all()
#     if request.POST:
#         formset = ClassLessonFormSet(request.POST,)
#         print(request.FILES)
#         if formset.is_valid():
#             for form in formset:
#                 x = form.save()
#                 student = Student.objects.filter().first()
#                 ClassLesson.objects.update(students = student)
#             return redirect('environment_education:class_detail')
#
#         else:
#             return render(request, 'environment_education/create_class_lesson_form.html', {"class_lesson_form": formset, 'class_lesson':class_lesson})
#
#     formset = ClassLessonFormSet()
#     return render(request, 'environment_education/create_class_lesson_form.html', {"class_lesson_formset": formset, 'class_lesson':class_lesson})