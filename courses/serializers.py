from rest_framework import serializers
from django.db.models import Avg

from . import models


class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }

        model = models.Evaluation
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # evaluations = EvaluationSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    evaluations = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='evaluation-detail',
    )

    average_evaluations = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = (
            'id',
            'title',
            'url',
            'created',
            'active',
            'evaluations',
            'average_evaluations'
        )

    def get_average_evaluations(self, object):
        average = object.evaluations.aggregate(Avg('evaluation')).get('evaluation__avg')

        if average is None:
            return 0
        return round(average * 2 ) / 2

