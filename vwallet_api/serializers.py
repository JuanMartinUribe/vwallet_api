from django.forms import SlugField
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from vwallet_main.models import MainUser, Pocket
from django.contrib.auth.models import User

class PocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pocket
        fields = ['name','quantity','status']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']

class MainUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    pockets = PocketSerializer(many=True)

    class Meta:
        model = MainUser
        fields = ['user','phone_number','pockets']
