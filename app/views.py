from rest_framework import status
from rest_framework.response import Response
from django.utils.text import slugify
from rest_framework.decorators import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from rest_framework.exceptions import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate, logout
from django.contrib.auth.signals import user_logged_in, user_logged_out
from rest_framework.generics import *
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import Permission, Group
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from .serializers import WalletKeySerializer








class WalletKeyView(APIView):


    def post(self, request):

        serializer = WalletKeySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()


        return Response(serializer.data, status=200)












