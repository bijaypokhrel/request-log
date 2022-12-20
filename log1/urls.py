from django.urls import path
from . import views

app_name = 'log1'

urlpatterns = [
    path('', views.all_logs, name='all_logs')
]
