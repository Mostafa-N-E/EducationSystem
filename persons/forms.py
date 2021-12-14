from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelMultipleChoiceField, ChoiceField, formset_factory
from django import forms

from .models import Student,ClassLesson

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = Student
#         fields = ('username', 'first_name', 'last_name', 'phone_number',
#                   'email', 'password1', 'password2','phone_number')
#


class ClassLessonForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ClassLessonForm,self).__init__(*args, **kwargs)
        self.fields['lesson'].help_text = "some"
        self.fields['cluss', 'professor' ,  'lesson','units_num', 'date_exam', 'code',].disabled = True
    class Meta:
        model = ClassLesson
        fields = ['cluss', 'professor' , 'students', 'lesson','units_num', 'date_exam', 'code',]
    # code = forms.IntegerField(max_length=10 ,min_value=10, label='کد کلاس درس', required=False)
    # student_code = forms.IntegerField(max_length=10 ,min_value=10, label='کد دانشجو', required=False)

ClassLessonFormSet = formset_factory(ClassLessonForm, extra=2, max_num=3)