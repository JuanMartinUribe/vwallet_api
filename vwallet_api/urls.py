from django.urls import path
from .views import PocketList, PocketDetail,MainUserList, UserList

app_name = 'vwallet_api'

urlpatterns = [
    path('',MainUserList.as_view(),name='userlist'),
]