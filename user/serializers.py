from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "fullname", "email", "phone", "password"]
        extra_kwargs = {
            'username': {'required': False},
            'fullname': {'required': False},
            'email': {'required': False},
            'phone': {'required': False},
            'password': {'write_only': True,
                         'required': False},
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            setattr(instance, key, value)
        instance.save()