from django.db import models
from environment_education.models import College
# Create your models here.

class Lidrary(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'کتابخانه'
    # name = models.CharField(max_length=100)
    collage = models.OneToOneField(College, on_delete=models.CASCADE, related_name='college_library')
    # members = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='members')


class Book(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'کتاب'
    name = models.CharField(max_length=100)
    is_rent = models.BooleanField(default=False)
    library = models.ForeignKey(Lidrary, on_delete=models.CASCADE, related_name='library')
    # rent = models.ManyToManyField(Rent,  related_name='rent', blank=True, null=True)


class Rent(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'امانت'
    # student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='student_rent')
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='book_rent')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()



