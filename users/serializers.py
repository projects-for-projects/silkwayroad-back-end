from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import UserAccount


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = UserAccount
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
