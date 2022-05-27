from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

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
            'confirm_password',
        ]

    def create(self, validated_data):
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError('Passwords are not same')
        user = User(alias=validated_data['alias'])
        user.set_password(validated_data['password'])
        user.save()
        return user
