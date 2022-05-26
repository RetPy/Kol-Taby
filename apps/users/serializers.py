from rest_framework.serializers import ModelSerializer

from apps.users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'alias',
            'first_name',
            'last_name',
            'patronymic',
            'birthday',
            'phone_number',
            'email',
            'password',
        ]

    def create(self, validated_data):
        user = User(alias=validated_data['alias'])
        user.set_password(validated_data['password'])
        user.save()
        return user
