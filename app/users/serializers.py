from rest_framework import serializers
from users import models


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for UserProfile
    """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'phone', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            name=validated_data['name'],
            phone=validated_data['phone'],
            password=validated_data['password']
        )

        return user
