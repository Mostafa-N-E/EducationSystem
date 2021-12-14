from django.db import models

from django.urls import reverse
# Create your models here.
class College(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'دانشکده'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'کلاس'
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='college_class')

    STATUS_CHOICE = [
            (1, 'Opened'),
            (0, 'Colsed'),
    ]
    status = models.PositiveIntegerField(choices=STATUS_CHOICE)
    def __str__(self):
        return self.name

class Lesson(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'درس'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name







    # def get_absolute_url(self):
    #     return reverse('environment_education:home')

    # DAY_OF_THE_WEEK = [
    #     (1, 'Monday'),
    #     (2, 'Tuesday'),
    #     (3, 'Wednesday'),
    #     (4, 'Thursday'),
    #     (5, 'Friday'),
    #     (6, 'Saturday'),
    #     (7, 'Sunday'),
    # ]
    # first_day_of_holding = models.PositiveIntegerField(choices=DAY_OF_THE_WEEK)
    # second_days_of_holding = models.PositiveIntegerField(choices=DAY_OF_THE_WEEK)

