from django.test import TestCase
from .models import User, Error
from datetime import datetime
from django.test import Client

# Create your tests here.
class TestUser(TestCase):
    def setUp(self) -> User:
        User.objects.create(first_name='aaa', last_name='last_aaa', email='aaa@teste.com', date_joined=datetime.now(),
                            is_staff=False, is_active=True)
        User.objects.create(first_name='bbb', last_name='last_bbb', email='bbb@teste.com', date_joined=datetime.now(),
                            is_staff=True, is_active=False)

    def test_get_full_name(self):
        user = User.objects.get(first_name='aaa')
        self.assertEqual(user.get_full_name(), 'aaa last_aaa')

    def test_user_email(self):
        user = User.objects.get(first_name='aaa')
        self.assertEqual(user.email, 'aaa@teste.com')

    def test_user_staff(self):
        user = User.objects.get(email='bbb@teste.com')
        self.assertEqual(user.is_active, False)


class TestFilter(TestCase):
    def setUp(self):
        user = User.objects.create(first_name='aaa', last_name='last_aaa', email='aaa@teste.com', date_joined=datetime.now(),
                            is_staff=False, is_active=True)
        Error.objects.create(title='Erro1', description='Desc erro1', level='error', environment='production',
                             address='127.0.0.1', created_at=datetime.now(), events=1, filed=False, user=user)
        Error.objects.create(title='Erro2', description='Desc erro2', level='debug', environment='homologation',
                             address='127.0.0.1', created_at=datetime.now(), events=1, filed=False, user=user)
        Error.objects.create(title='Erro3', description='Desc erro3', level='debug', environment='production',
                             address='127.0.0.1', created_at=datetime.now(), events=2, filed=False, user=user)
        Error.objects.create(title='Erro4', description='Desc erro4', level='warning', environment='development',
                             address='127.0.0.1', created_at=datetime.now(), events=1, filed=False, user=user)


    def test_error(self):
        error = Error.objects.get(title='Erro1')
        self.assertEqual(error.title, 'Erro1')

    def test_filter_env(self):
        c = Client()
        response = c.get('/api/errors/', {'environment': 'production'})
        self.assertEqual(len(response.json()), 2)

    def test_filter_level(self):
        c = Client()
        response = c.get('/api/errors/', {'level': 'error'})
        title = response.json()[0].get('title')
        self.assertEqual(title, 'Erro1')

    def test_filter_search(self):
        c = Client()
        response = c.get('/api/errors/', {'search_for': 'description', 'search': 'erro4'})
        title = response.json()[0].get('title')
        self.assertEqual(title, 'Erro4')



