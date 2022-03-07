from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from vwallet_main.models import MainUser, Pocket

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