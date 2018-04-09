from django.shortcuts import render

# Create your views here.


from django.views.generic import View
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q



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











class UserInfo(View):
    '''
        个人信息中心
    '''
    pass






