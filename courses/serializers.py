from rest_framework import serializers
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

    class Meta:
        model = models.Course
        fields = (
            'id',
            'title',
            'url',
            'created',
            'active',
            'evaluations',
        )
