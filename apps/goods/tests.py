import os

import sys

from django.db.models import Q
from django.test import TestCase


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "daydah_store2.settings")

import django
from goods.models import Goods
django.setup()
value = 123
queryset = Goods.objects.all()
# Create your tests here.
queryset = queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
    category__parent_category__parent_category_id=value))

print(queryset)