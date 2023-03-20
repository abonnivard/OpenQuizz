from django.contrib import admin
from django.urls import path
from .views import dashboard, suppression

app_name = 'administrateur'

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('suppression/', suppression, name="suppression"),
]
