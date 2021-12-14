from django.contrib import admin
from .models import Class,College,Lesson

from django.contrib import messages
from django.utils.translation import ngettext
# Register your models here.
class ClassInline(admin.StackedInline):
    model = Class
    extra = 0
    max_num = 5

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name',]
    fields = ['name',]
    search_fields = ['name',]
    #inlines = [ProfessorInline,]

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    fields = ['name',]
    search_fields = ['name', ]
    inlines = [ClassInline, ]


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name','status',]
    fields = ['name','college' ,'status',]
    search_fields = ['name',]

    @admin.action(description="تغییر وضعیت سفارش به  'دایر'")
    def change_statusــopen(self, request, queryset):
        update = queryset.update(status=1)
        self.message_user(request, ngettext(
            '  %d مورد با موفقیت تغییر یافت', '  %d مورد با موفقیت تغییر یافتند',
            update, ) % update, messages.SUCCESS)

    @admin.action(description="تغییر وضعیت سفارش به  'تعطیل'")
    def change_statusــColsed(self, request, queryset):
        update = queryset.update(status=0)
        self.message_user(request, ngettext(
            '  %d مورد با موفقیت تغییر یافت', '  %d مورد با موفقیت تغییر یافتند',
            update, ) % update, messages.SUCCESS)

    actions = [change_statusــColsed,change_statusــopen,]


