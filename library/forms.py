from django.forms import forms
from django import forms
from .models import Rent,Book
from persons.models import Student


# colleges = list(College.objects.all())
# college_choices = [(College.objects.get(pk=college.pk),college.name) for college in colleges]
# college_choices = [college for college in colleges]
# class Book_Form(forms.Form):
#     name = forms.CharField(label='عنوان پست', max_length=50, required=False)
#     class Meta:
#         model = Book
#         # exclude = ('college',)
#         fields = ('name',)
# class Rent_Form(forms.Form):
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     # self.instance = Student()
#     #     # self.fields['lesson'].help_text = "some"
#     #     self.files['student',].choices = 'self'
#     #     self.files['student',].disabled = True
#     #
#
#     start_date = forms.DateTimeField(label='تاریخ امانت گرفتن')
#     end_date = forms.DateTimeField(label='تاریخ تحویل',)
#     class Meta:
#         model = Rent
#         # exclude = ('college',)
#         fields = ('student','start_date','end_dare',)
    #
    #
    # def clean_student(self):
    #     student = self.cleaned_data.get('student')
    #     try:
    #         # password_validation.validate_password(password1, self.instance)
    #         student_instans = Student.objects.get(name=self.request.user)
    #     except forms.ValidationError as error:
    #
    #         # Method inherited from BaseForm
    #         self.add_error('student_instans', error)
    #     return student_instans

# class PostSearchForm(forms.Form):
#     """
#     This is a form of professional search.
#     """
#     title = forms.CharField(label='عنوان پست', max_length=50, required=False)
#     tag = forms.CharField(max_length=30, label='برچسب', required=False)
#     first_name = forms.CharField(label='نام نویسنده', required=False)
#     last_name = forms.CharField(label='نام خانوادگی نویسنده', required=False)
#     word = forms.CharField(max_length=50, label='کلمه کلیدی در پست', required=False)
class Rent_Form(forms.Form):
    """
    This is a form of professional search.
    """
    book = forms.CharField(label='کتابو', max_length=50, required=False )
    start_date = forms.DateTimeField(label='تاریخ امانت گرفتن')
    end_date = forms.DateTimeField(label='تاریخ تحویل', )

    # def clean_student(self):
    #     student = self.cleaned_data.get('student')
    #     try:
    #         # password_validation.validate_password(password1, self.instance)
    #         student_instans = Student.objects.get(username=student)
    #     except forms.ValidationError as error:
    #
    #         # Method inherited from BaseForm
    #         self.add_error('student_instans', error)
    #     return student_instans.id