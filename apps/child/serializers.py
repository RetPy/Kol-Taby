from rest_framework import serializers

from apps.child.models import Child, Answer
from apps.users.models import User


class ChildSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_staff=False), allow_null=True)

    class Meta:
        model = Child
        fields = [
            'id',
            'first_name',
            'last_name',
            'patronymic',
            'birthday',
            'parents_fio',
            'gender',
            'parents_phone_number',
            'parents_email',
            'address',
            'diagnosis',
            'visit_weekday',
            'visit_time',
            'exercises',
            'employee',
            'questions',
        ]


class AnswerSerializer(serializers.ModelSerializer):
    employee = serializers.CharField(
        read_only=True
    )

    class Meta:
        model = Answer
        fields = [
            'id',
            'date',
            'employee',
            'child',
            'quiz',
            'image_1',
            'image_2',
            'image_3',
        ]


class UserAnswerSerializer(serializers.ModelSerializer):
    employee = serializers.CharField(
        read_only=True
    )
    child = ChildSerializer(
        read_only=True
    )

    class Meta:
        model = Answer
        fields = [
            'id',
            'date',
            'employee',
            'child',
            'quiz',
            'image_1',
            'image_2',
            'image_3',
        ]
