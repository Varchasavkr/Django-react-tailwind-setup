from django.contrib import admin
from django.urls import path,include
from firstserver import views

urlpatterns = [
   
    path('Student', views.StudentList.as_view()),
    path('',views.index,name='se' ),
]
