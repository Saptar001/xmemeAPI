from django.urls import path,include

from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('add_data_form_submission/',views.add_data_form_submission,name='add_data_form_submission'),
]