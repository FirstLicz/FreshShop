from django.test import TestCase

# Create your tests here.


import sys
import os

pwd= os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.abspath(os.path.join(pwd,'..')))
sys.path.append(pwd)
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Freshshop.settings')
import django
django.setup()

from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.filter(username='admin')

token = Token.objects.create(user=user[0])
print(token.key)
