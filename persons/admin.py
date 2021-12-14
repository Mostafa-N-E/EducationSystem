from django.contrib import admin
from .models import Professor,Student,UniversityStaff,UnivercityPersident,ClassLesson

# Register your models here.
@admin.register(UnivercityPersident)
class UnivercityPersidentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', ]
    fields = ['username', 'first_name', 'last_name', 'phone_number', 'email',]
    search_fields = ['phone_number', ]

@admin.register(UniversityStaff)
class UniversityStaffAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', ]
    fields = ['username', 'first_name', 'last_name', 'phone_number',  'email','college',]
    search_fields = ['phone_number', ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', ]
    fields = ['username', 'first_name', 'last_name', 'phone_number', 'email','college']
    search_fields = ['phone_number', ]

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', ]
    fields = ['username', 'first_name', 'last_name', 'phone_number',  'email','lessons']
    search_fields = ['phone_number', ]

@admin.register(ClassLesson)
class ClassLessonAdmin(admin.ModelAdmin):
    list_display = ['professor','lesson','code']
    fields = ['cluss','professor','students','lesson','code',]
    search_fields = ['cluss','professor','lesson',]