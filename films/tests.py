from django.test import TestCase, RequestFactory
import json

from .views import *

# Create your tests here.
class SimpleTest(TestCase):
#    reset_sequences = True

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_GET_genres(self):
        # Create an instance of a GET request.
        request = self.factory.get('/genres')
        # Test my_view() as if it were deployed at /genres
        response = genre_list(request)
        self.assertEqual(response.status_code, 200)


    def test_POST_genres(self):
        # Create an instance of a post request.
        request = self.factory.post('/genres', {"description": "Fantasy"}, format='json')
        # Test genre_list() as if it were deployed at /genres
        response = genre_list(request)
        # test status
        self.assertEqual(response.status_code, 201)
        # make sure it exists
        self.assertEqual(response.data['description'], 'Fantasy')


    def test_PUT_genres(self):
        # Create an instance of a post request.
        request = self.factory.post('/genres', {"id": 1, "description": "Fantasy"})
        response = genre_list(request)
        self.assertEqual(response.status_code, 201)
        response.render()

        # Create an instance of a put request.
        request = self.factory.put('/genres/1', {"id": 1, "description": "ffantasy"})
        # Test genre_detail() as if it were deployed at /genres
        response = genre_detail(request, pk=1)
        self.assertEqual(response.status_code, 200)


    def test_DELETE_genres(self):
        # Create an instance of a post request.
        request = self.factory.post('/genres/1', {"description": "Fantasy"})
        response = genre_list(request)
        self.assertEqual(response.status_code, 201)
        response.render()

        # Create an instance of a delete request.
        request = self.factory.delete('/genres')
        # Test genre_detail() as if it were deployed at /genres
        response = genre_detail(request, pk=1)
        # test status
        self.assertEqual(response.status_code, 204)

    def test_GET_theaters(self):
        # Create an instance of a GET request.
        request = self.factory.get('/theaters')
        # Test theater_list() as if it were deployed at /theaters
        response = theater_list(request)
        self.assertEqual(response.status_code, 200)

    def test_POST_theaters(self):
        # Create an instance of a post request.
        request = self.factory.post('/theaters',
              {
                 "name": "Theater Name",
                 "city": "Theater City",
                 "state": "OR",
                 "num_screens": 3,
                 "digital": True,
                 "comment_txt": "This is a theater comment"
                 }, format='json')
        # Test theater_list() as if it were deployed at /theaters
        response = theater_list(request)
        # test status
        self.assertEqual(response.status_code, 201)
        #make sure it exists
        self.assertEqual(response.data['name'], 'Theater Name' )

    def test_PUT_theaters(self):
        # Create an instance of a post request.
        request = self.factory.post('/theaters/1',
                  {
                      "name": "Theater Name",
                      "city": "Theater City",
                      "state": "OR",
                      "num_screens": 3,
                      "digital": True,
                      "comment_txt": "This is a theater comment"
                  }, format='json')
        response = theater_list(request)
        self.assertEqual(response.status_code, 201)
        response.render()

        # Create an instance of a put request.
        request = self.factory.put('/theaters/1', {"id":1, "name":"Avalon Theater"})
        # Test theater_detail() as if it were deployed at /theaters
        response = theater_detail(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_DELETE_theaters(self):
        # Create an instance of a post request.
        request = self.factory.post('/theaters',
                  {
                      "name": "Theater Name",
                      "city": "Theater City",
                      "state": "OR",
                      "num_screens": 3,
                      "digital": True,
                      "comment_txt": "This is a theater comment"
                  }, format='json')
        response = theater_list(request)
        self.assertEqual(response.status_code, 201)
        response.render()

        # Create an instance of a delete request.
        request = self.factory.delete('/theaters/1')
        # Test theater_detail() as if it were deployed at /theaters
        response = theater_detail(request, pk=1)
        # test status
        self.assertEqual(response.status_code, 204)

    def test_GET_films(self):
        # Create an instance of a GET request.
        request = self.factory.get('/films')
        # Test film_list() as if it were deployed at /films
        response = film_list(request)
        self.assertEqual(response.status_code, 200)


    def test_POST_films(self):
        # Create an instance of a post request.
        request = self.factory.post('/genres', {"description": "Fantasy"}, format='json')
        response = genre_list(request)
        # Create an instance of a post request.
        request = self.factory.post('/films',
                                    {
                                        "title": "Film Title",
                                        "year_prod": 2000,
                                        "genre": 1,
                                        "theaters": []
                                    }, format='json')
        # Test film_list() as if it were deployed at /films
        response = film_list(request)
        # test status
        self.assertEqual(response.status_code, 201)
        # make sure it exists
        self.assertEqual(response.data['title'], 'Film Title')


    def test_PUT_films(self):
        # Create an instance of a post request.
        request = self.factory.post('/films/1',
                                    {
                                        "title": "Film Title",
                                        "year_prod": 2000,
                                        "genre": 1,
                                        "theaters": []
                                    }, format='json')
        response = film_list(request)
        self.assertEqual(response.status_code, 201)
        response.render()

        # Create an instance of a put request.
        request = self.factory.put('/films/1', {"id": 1, "name": "Capricorn One"})
        # Test film_detail() as if it were deployed at /films
        response = film_detail(request, pk=1)
        self.assertEqual(response.status_code, 200)


    def test_DELETE_films(self):
        # Create an instance of a post request.
        request = self.factory.post('/genres', {"description": "Fantasy"}, format='json')
        response = genre_list(request)
        # Create an instance of a post request.
        request = self.factory.post('/films',
                                    {
                                        "title": "Film Title",
                                        "year_prod": 2000,
                                        "genre": 1,
                                        "theaters": []
                                    }, format='json')
        response = film_list(request)
        self.assertEqual(response.status_code, 201)
        response.render()

        # Create an instance of a delete request.
        request = self.factory.delete('/films/1')
        # Test film_detail() as if it were deployed at /films
        response = film_detail(request, pk=1)
        # test status
        self.assertEqual(response.status_code, 204)
