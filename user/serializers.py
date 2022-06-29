from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "fullname", "email", "phone", "password", "permissions"]
        extra_kwargs = {
            'username': {'required': False},
            'fullname': {'required': False},
            'email': {'required': False},
            'phone': {'required': False},
            'password': {'write_only': True,
                         'required': False},
            'permissions': {'required': False},
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            fullname=validated_data['fullname'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            permissions=validated_data['permissions']
        )
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