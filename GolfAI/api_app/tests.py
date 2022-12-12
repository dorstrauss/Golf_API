from django.test import TestCase
from functions import *
from datetime import *

swing_data = {'username': 'dr34h@gm252.com',
              'time': datetime.now(),
              'speed': 117,
              'shaft': 'Stiff',
              'weight': 602,
              'type': 'Wood'
              }

save_swing_data(swing_data)


# Create your tests here.
