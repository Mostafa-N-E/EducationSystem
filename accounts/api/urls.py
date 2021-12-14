from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginAPIView, name='s_college_list'),

]
