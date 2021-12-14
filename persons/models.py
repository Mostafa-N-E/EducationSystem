from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Max
from environment_education.models import College,Lesson, Class
from library.models import Rent
User = get_user_model()
# Create your models here.
class UnivercityPersident(User):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'رییس دانشگاه'
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.username

class UniversityStaff(User):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'کارمند دانشگاه'
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    college = models.ForeignKey(College, on_delete=models.CASCADE,related_name='staff_college')

    def __str__(self):
        return self.username

class Professor(User):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'استاد'
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson, related_name='professor_lessons',null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    address = models.TextField(null=True,blank=True)
    # contract = models.FileField(upload_to='contracts/', blank=True, null=True, default=None)

    def __str__(self):
        return self.username


def count_numbers():
    pass
class Student(User):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'دانشجو'
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson, related_name='lessons')
    college = models.ForeignKey(College, on_delete=models.CASCADE,related_name='student_college')
    date_of_entery = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    rented_book = models.ManyToManyField(Rent,  related_name='rented_books', blank=True, null=True)

    last_visit = models.DateTimeField( blank=True, null=True)
    created_by = models.ForeignKey(UniversityStaff, on_delete=models.CASCADE,related_name='student_created_by', null=True, blank=True)
    is_email_active = models.BooleanField(verbose_name='is_email_active', default=False, blank=True, null=True)

    # score = models.IntegerField()

    # student_code = models.IntegerField(default=count_numbers)
    # def count_numbers(self):
    #     query = list(self.objects.order_by('-number')[:1])
    #     return query[0] + 1 if query else 0

    def __str__(self):
        return self.username




class ClassLesson(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'کلاس برگزاری درس'
    cluss = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='clUss')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='professor')
    students = models.ManyToManyField(Student, related_name='students')

    # scortes = models.ManyToManyField(Student.score, related_name='students')

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson')
    units_num = models.IntegerField(null=True, blank=True)
    date_exam = models.DateTimeField(null=True, blank=True)
    code = models.IntegerField()

    def __str__(self):
        return f"{self.cluss.name} -- {self.lesson} -- {self.professor}"
# class UserInfo(models.Model):
#     phone = models.IntegerField('شماره تلفن', null=True, blank=True)
#     # photo = models.ImageField(verbose_name='عکس کاربر', upload_to='uploads/user_photo',default='/static/images/')
#     user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='آیدی کاربری', related_name='info',
#                                 null=True)
#
#     def __str__(self):
#         return self.user

