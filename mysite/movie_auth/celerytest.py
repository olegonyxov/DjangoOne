import unittest
from unittest.mock import patch, Mock
from .models import User
from tasks import change_flag

class CeleryTest(unittest.TestCase):
    def test_change_flag(self):
        my_queryset= Mock(User.objects.all()[:10])
        my_queryset.update(is_notified=False)
        result=change_flag(my_queryset)
        expected_result = 0
        self.assertEqual(expected_result, result)



