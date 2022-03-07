
from rest_framework import generics
from vwallet_main.models import Pocket,MainUser
from .serializers import PocketSerializer,MainUserSerializer

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