import unittest
from django.test import Client
from views import MovieViewSet


class TestMovie(unittest.TestCase):

    def test_list(self):
        c = Client()
        request= c.get('http://127.0.0.1:8000/api/v1/movies/')
        move = MovieViewSet.list(request)
        self.assertEqual(move.status_code,200)

    def test_add(self):
        c = Client()
        params = c.post(title='title',year="2000",pub_date="12-12-2000")
        move=MovieViewSet.create(params)
        self.assertNotEqual(move.status_code,200)








