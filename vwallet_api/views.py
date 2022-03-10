
from rest_framework import generics
from vwallet_main.models import Pocket,MainUser
from .serializers import PocketSerializer,MainUserSerializer, UserSerializer
from django.contrib.auth.models import User
 

# Create your views here.

class PocketList(generics.ListCreateAPIView):
    queryset = Pocket.pocketobjects.all()
    serializer_class = PocketSerializer
    pass

class PocketDetail(generics.RetrieveDestroyAPIView):
    queryset = Pocket.objects.all()
    serializer_class = PocketSerializer
    pass
class MainUserList(generics.ListCreateAPIView):
    queryset = MainUser.mainuserobjects.all()
    serializer_class = MainUserSerializer
    pass

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pass
class MainUserDetail(generics.RetrieveDestroyAPIView):
    queryset = MainUser.objects.all()
    serializer_class = MainUserSerializer
    pass