from django.urls import path, include

from . import views

app_name = 'environment_education'

urlpatterns = [
    path('college/create_class/', views.create_class, name="create_class"),

]

# path('college/select-class/', views.SelectClassLesson, name='select_class')
