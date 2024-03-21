# myapp/urls.py

# ORM_model_App/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Student URLS
    path('students/', views.student_list),
    path('students/create/', views.student_create),
    path('students_delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('students/update/<int:pk>/', views.student_update),

    path('teachers/', views.teacher_list),
    path('teachers/create/', views.teacher_create),
    path('teachers_delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),
    path('teachers/update/<int:pk>/', views.teacher_update),


    path('management/', views.management_list),
    path('management/create/', views.management_create),
    path('management_delete/<int:pk>/', views.management_delete, name='management_delete'),
    path('management/update/<int:pk>/', views.management_update),

    path('itdepartment/', views.ITDepartment_list),
    path('itdepartment/create/', views.ITDepartment_create),
    path('itdepartment_delete/<int:pk>/', views.ITDepartment_delete, name='Record_delete'),
    path('itdepartment/update/<int:pk>/', views.ITDepartment_update),


    path('BBITdepartment/', views.BBIT_list),
    path('BBITdepartment/create/', views.BBIT_create),
    path('BBITdepartment_delete/<int:pk>/', views.BBIT_delete, name='Record_delete'),
    path('BBITdepartment/update/<int:pk>/', views.BBIT_update),


    ]
