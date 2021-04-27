from rest_framework import serializers
from Profile.models import User
from rest_framework.authtoken.models import Token


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'date', 'balance', 'username'
        )
    