from rest_framework import serializers




from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """a serialzer for our user profile"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """create and return new user"""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])

        user.save()
        return user

#class LoginUserSerializer(serializers.Serializer):

 #   person = serializers.CharField(max_length=255)
