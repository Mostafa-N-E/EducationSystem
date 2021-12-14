from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),

    path('accounts/', include('accounts.api.urls')),
    path('environment_education/', include('environment_education.api.urls')),
    path('persons/', include('persons.api.urls')),
    path('library/', include('library.api.urls')),

]
