from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from application.quickstart.serializers import UserSerializer, GroupSerializer,MenuSerializer
from rest_framework.permissions import IsAuthenticated
from application.quickstart.models import Menus
import datetime


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GetDailyMenus(viewsets.ModelViewSet):
    """
    API endpoint that allows menus corresponding to current day to be viewed
    """
    permission_classes = (IsAuthenticated,)
    queryset = Menus.objects.filter(day=datetime.datetime.today().weekday())
    serializer_class = MenuSerializer

