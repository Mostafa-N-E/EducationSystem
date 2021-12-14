from django.urls import path, include
from . import views


urlpatterns = [
    # college
    path('college_list/', views.college_list, name='s_college_list'),
    path('college-detail/<int:pk>', views.college_detail, name='s_college_detail'),
]
