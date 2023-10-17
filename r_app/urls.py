from django.urls import path

from . import admin
from .views import index, submit_form

urlpatterns = [
    path('', index, name='index'),
    # path('submit_form/', submit_form, name='submit_form'),

]