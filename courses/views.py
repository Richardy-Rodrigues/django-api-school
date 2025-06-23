from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models, serializers


class CourseAPIView(APIView):
    """
    Courses API Rest
    """

    def get(self, request):
        courses = models.Course.objects.all()
        serializer = serializers.CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EvaluationAPIView(APIView):
    """
    Evaluations API Rest
    """

    def get(self, request):
        evaluations = models.Evaluation.objects.all()
        serializer = serializers.EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

