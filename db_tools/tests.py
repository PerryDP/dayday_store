import os

import sys

from django.db.models import Q
from django.test import TestCase


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "daydah_store2.settings")

import django
django.setup()
from goods.models import Goods
value = 123
queryset = Goods.objects.all()
# Create your tests here.
queryset = queryset.filter(Q(category_id=123) )

print(queryset)