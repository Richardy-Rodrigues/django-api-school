from django.urls import path

from . import views

urlpatterns = [
    path('courses/', views.CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', views.CourseAPIView.as_view(), name='detail_course'),
    path('courses/<int:course_pk>/evaluations/', views.EvaluationsAPIView.as_view(), name='course_evaluations'),
    path('courses/<int:course_pk>/evaluations/<int:evaluation_pk>/', views.EvaluationAPIView.as_view(), name='course_evaluation'),

    path('evaluations/', views.EvaluationsAPIView.as_view(), name='evaluations'),
    path('evaluations/<int:evaluation_pk>/', views.EvaluationAPIView.as_view(), name='detail_evaluation'),
]