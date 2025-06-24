from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404

from . import models, serializers


class CoursesAPIView(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class EvaluationsAPIView(generics.ListCreateAPIView):
    queryset = models.Evaluation.objects.all()
    serializer_class = serializers.EvaluationSerializer

    def get_queryset(self):
        if (self.kwargs.get('course_pk')):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()

class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Evaluation.objects.all()
    serializer_class = serializers.EvaluationSerializer

    def get_object(self):
        if (self.kwargs.get('course_pk')):
            return get_object_or_404(self.get_queryset(), course_id=self.kwargs.get('course_pk'), pk=self.kwargs.get('evaluation_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('evaluation_pk'))