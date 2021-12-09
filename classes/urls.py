from django.urls import path
from . import views

urlpatterns = [
    path('classes/', views.seances , name='class_list'),
    path('seances/<str:pk>/', views.seance_detail, name='seance_detail'),

    path('setToPresent/', views.set_student_present, name='setToPresent'),
    path('setToAbsent/', views.set_student_absent, name='setToAbsent'),
]

