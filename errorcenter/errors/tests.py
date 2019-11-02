from .models import User, Error
from rest_framework.test import APITestCase, APIClient, RequestsClient
from rest_framework.authtoken.models import Token
from django.test import TestCase

# Create your tests here.
class TestUser(TestCase):
    def setUp(self) -> User:
        self.user1 = User.objects.create_user(first_name='aaa', last_name='last_aaa', email='aaa@teste.com', password='python123a')
        self.user2 = User.objects.create_user(first_name='bbb', last_name='last_bbb', email='bbb@teste.com', password='python123b')

    def test_get_full_name(self):
        user = User.objects.get(first_name='aaa')
        self.assertEqual(user.get_full_name(), 'aaa last_aaa')

    def test_user_email(self):
        user = User.objects.get(first_name='aaa')
        self.assertEqual(user.email, 'aaa@teste.com')


class TestAuthentication(APITestCase):
    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=True)
        self.user = User.objects.create(first_name='Camila', last_name='Sakata', email='camila@teste.com', password='camilasakata123')
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def test_token_authentification(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/errors/')
        self.assertEqual(response.status_code, 200)


class TestAPIRequests(APITestCase):
    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=True)
        self.user = User.objects.create(first_name='Camila', last_name='Sakata', email='camila@teste.com', password='camilasakata123')
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        Error.objects.create(title='Erro1', description='Desc erro1', level='error', environment='production',
                             address='127.0.0.1', events=1, user=self.user)
        Error.objects.create(title='Erro2', description='Desc erro2', level='debug', environment='homologation',
                             address='127.0.0.1', events=1, user=self.user)
        Error.objects.create(title='Erro3', description='Desc erro3', level='debug', environment='production',
                             address='127.0.0.1', events=50, user=self.user)
        Error.objects.create(title='Erro4', description='Desc erro4', level='warning', environment='development',
                             address='127.0.0.1', events=10, user=self.user)

    def test_post_error(self):
        response = self.client.post('/api/errors/', {
            'id': 10,
            'title': 'Erro Teste',
            'description': 'Desc do erro teste',
            'level': 'debug',
            'environment': 'development',
            'address': '127.0.0.1',
            'events': 1,
            'user': self.user.id,
        })
        self.assertEqual(response.status_code, 201)

    def test_filter_env(self):
        response = self.client.get('/api/errors/?environment=production', format='json')
        self.assertEqual(len(response.data), 2)

    def test_filter_order_freq(self):
        response = self.client.get('/api/errors/?order_by=-events', format='json')
        self.assertEqual(response.data[0]['title'], 'Erro3')

    def test_filter_order_level(self):
        response = self.client.get('/api/errors/?order_by=-level', format='json')
        self.assertEqual(response.data[0]['title'], 'Erro4')

    def test_filter_search(self):
        response = self.client.get('/api/errors/?search_for=description&search=erro2', format='json')
        self.assertEqual(response.data[0]['title'], 'Erro2')

    def test_archive_error(self):
        response = self.client.patch('/api/errors/1/archive/', data={'filed':True}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_error(self):
        response = self.client.patch('/api/errors/1/delete/', data={'delete':True}, format='json')
        self.assertEqual(response.status_code, 200)





