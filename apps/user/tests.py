import sys

import os
from django.test import TestCase

# Create your tests here.
from daydah_store2.settings import BASE_DIR

print(sys.path)
print('================')
sys.path.insert(0,BASE_DIR)
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
sys.path.insert(0,os.path.join(BASE_DIR,'extra_app'))
print(sys.path)
