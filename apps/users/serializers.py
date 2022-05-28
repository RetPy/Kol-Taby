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
        user = User(
            alias=validated_data['alias'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            patronymic=validated_data['patronymic'],
            birthday=validated_data['birthday'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CurrentUserSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=1000)


class CheckAliasSerializer(serializers.Serializer):
    alias = serializers.CharField()
