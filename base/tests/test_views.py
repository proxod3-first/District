from django.test import TestCase
from django.urls import reverse
from base.models import *
from base.views import *
from django.core.cache import cache

from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware


# Tests for views


class TopicsPageTest(TestCase):
    def setUp(self):
        self.topic1 = Topic.objects.create(name='Test Topic 1')
        self.topic2 = Topic.objects.create(name='Test Topic 2')

    def test_topics_page_without_query(self):
        response = self.client.get(reverse('topics'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['topics'],
            [repr(self.topic1), repr(self.topic2)],
            ordered=False
        )

    def test_topics_page_with_query(self):
        response = self.client.get(reverse('topics'), {'q': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['topics'],
            [repr(self.topic1), repr(self.topic2)],
            ordered=False
        )



class LogoutUserViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='john', email='john@doe.com', password='password')

    def test_logout_user(self):
        request = self.factory.get(reverse('logout'))
        request.user = self.user
        SessionMiddleware().process_request(request)
        request.session.save()

        response = logoutUser(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home'))

    def test_logout_user_cache(self):
        cache.clear()
        request = self.factory.get(reverse('logout'))
        request.user = self.user
        SessionMiddleware().process_request(request)
        request.session.save()

        response1 = logoutUser(request)
        response2 = logoutUser(request)
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response2.status_code, 302)
        self.assertNotEqual(response1, response2)

        cache.clear()
        response3 = logoutUser(request)
        self.assertEqual(response3.status_code, 302)
        self.assertNotEqual(response1, response3)
