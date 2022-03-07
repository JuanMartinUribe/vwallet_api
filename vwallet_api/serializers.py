from django.forms import SlugField
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from vwallet_main.models import MainUser, Pocket
from django.contrib.auth.models import User

class PocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pocket
        fields = ('id','user','name','quantity','status')

class MainUserSerializer(serializers.ModelSerializer):
    
    user = serializers.SlugRelatedField(
        read_only = True,
        slug_field='username',
    
    )
    
    pockets = serializers.StringRelatedField(many=True)

    
    class Meta:
        model = MainUser
        fields = ['user','phone_number','pockets']
class UserSerializer(serializers.ModelSerializer):
    pockets = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'id','pockets')