import datetime
from django.test import TestCase

# Create your tests here.
a = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
print(a)
print(type(a))