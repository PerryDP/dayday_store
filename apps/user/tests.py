import re
import sys

import os
from django.test import TestCase

# Create your tests here.
import string
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
a = 'a123456'
if re.search(r'.*[a-z].*[A-Z].*]', a):
    print('=========')
