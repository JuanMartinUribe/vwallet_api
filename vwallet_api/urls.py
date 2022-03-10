from django.urls import path
from .views import MainUserDetail, PocketList, PocketDetail,MainUserList, UserList

app_name = 'vwallet_api'

urlpatterns = [
    path('',MainUserList.as_view(),name='userlist'),
    path('<int:pk>',MainUserDetail.as_view(),name='userdetail')
]