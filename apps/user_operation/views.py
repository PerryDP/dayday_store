from django.shortcuts import render
from rest_framework import mixins, viewsets, status, serializers
# Create your views here.
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from goods.serizlizers import GoodsSerizlizer
from user_operation.models import UserFav, UserAddress
from user_operation.serializers import UserFavSerializer, UserAddressSer, UserFavDetailSerializer

from utils.permissions import IsOwnerOrReadOnly


class UserFavViewset(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                     mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = "goods_id"

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer

        return UserFavSerializer


class UserAddressViewset(viewsets.ModelViewSet):
    serializer_class = UserAddressSer

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
