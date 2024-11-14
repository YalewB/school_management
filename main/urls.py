from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('director_dashboard/', views.director_dashboard, name='director_dashboard'),
    path('parent_dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('finance_dashboard/', views.finance_dashboard, name='finance_dashboard'),
]