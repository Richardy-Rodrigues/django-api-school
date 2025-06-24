from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action

from . import models, serializers


"""
VERSION 1
"""
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


"""
VERSION 2
"""
class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    @action(detail=True, methods=['get'])
    def evaluations(self, request, pk=None):
        self.pagination_class.page_size = 5
        evaluations = models.Evaluation.objects.filter(course_id=pk)
        page = self.paginate_queryset(evaluations)

        if page is not None:
            serializer = serializers.EvaluationSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = models.Evaluation.objects.all()
    serializer_class = serializers.EvaluationSerializer
