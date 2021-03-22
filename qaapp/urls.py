from django.urls import path
from django.conf.urls import url

# from .views import (
#     TmpView
# )

from . import views

app_name = 'qaapp'

urlpatterns = [
    # url(r'^tmp/$', views.tmp, name='tmpview'),
    # url(r'^new/$', views.tmp, name='tmpview'),
    url(r'^new/$', views.tmp, name='new'),
    url(r'^dev/$', views.dev, name='devview'),
    # url(r'^edit/$', views.edit, name='editview'),
    path('edit/<question_id>/', views.edit, name='question_edit'),
    path('questions/<question_id>/answer_new/', views.answer_new, name='answer_new'),
    path('answers/<answer_id>/edit/', views.answer_edit, name='answer_edit'),
]

