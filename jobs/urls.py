from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/jobs/', views.job_list, name='job_list'),
    path('api/post-job/', views.api_post_job, name='api_post_job'),  # JSON API
    path('post-job/', views.post_job, name='post_job'),              # HTML Form
    path('job/<int:pk>/', views.job_detail, name='job_detail'),      # ✅ Use only 'pk'
]
