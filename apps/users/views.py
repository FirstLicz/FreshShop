from django.shortcuts import render

# Create your views here.


from django.views.generic import View
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.generics import mixins
from rest_framework.response import Response
from rest_framework import status


from .serializers import VerifyUserSerializer


User = get_user_model()

class Custombackend(ModelBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    自定义用户验证
    """
    def authenticate(self,username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SendVerifyCodeViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
        发送短信验证码
    '''
    serializer_class = VerifyUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']
        '''
        发送验证码
        '''

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)





class UserInfo(View):
    '''
        个人信息中心
    '''
    pass






