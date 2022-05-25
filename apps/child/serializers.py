from rest_framework.serializers import ModelSerializer

from apps.child.models import Child, Answer


class ChildSerializer(ModelSerializer):

    class Meta:
        model = Child
        fields = '__all__'


class AnswerSerializer(ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'
