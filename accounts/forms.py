from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from environment_education.models import College
from persons.models import Student, UniversityStaff


colleges = list(College.objects.all())
college_choices = [(College.objects.get(pk=college.pk),college.name) for college in colleges]
# college_choices = [college for college in colleges]
class SignUp_STU_Form(UserCreationForm):
    first_name = forms.CharField(max_length=50,required=False)
    last_name = forms.CharField(max_length=50,required=False)
    email = forms.EmailField(max_length=50)
    college = forms.ChoiceField(choices=college_choices)

    class Meta:
        model = Student
        # exclude = ('college',)
        fields = ('username', 'first_name', 'last_name', 'phone_number',
                  'email', 'password1', 'password2','phone_number','college')

    def clean_college(self):
        college = self.cleaned_data.get('college')
        try:
            # password_validation.validate_password(password1, self.instance)
            college_instans = College.objects.get(name=college)
        except forms.ValidationError as error:

            # Method inherited from BaseForm
            self.add_error('college_instans', error)
        return college_instans



class SignUp_STF_Form(UserCreationForm):
    first_name = forms.CharField(max_length=50,required=False)
    last_name = forms.CharField(max_length=50,required=False)
    email = forms.EmailField(max_length=50)
    college = forms.ChoiceField(choices=college_choices)

    class Meta:
        model = UniversityStaff
        # exclude = ('college',)
        fields = ('username', 'first_name', 'last_name', 'phone_number',
                  'email', 'password1', 'password2','phone_number','college')

    def clean_college(self):
        college = self.cleaned_data.get('college')
        try:
            # password_validation.validate_password(password1, self.instance)
            college_instans = College.objects.get(name=college)
        except forms.ValidationError as error:

            # Method inherited from BaseForm
            self.add_error('college_instans', error)
        return college_instans


class StudentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StudentForm).__init__(*args, **kwargs)
        # self.fields['lesson'].help_text = "some"
        self.fields['first_name', 'last_name', 'phone_number',].disabled = True
    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', ]