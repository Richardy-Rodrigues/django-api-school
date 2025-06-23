from django.urls import path

from . import views

urlpatterns = [
    path('courses/', views.CourseAPIView.as_view(), name='courses'),
    path('evaluations/', views.EvaluationAPIView.as_view(), name='evaluations'),
]