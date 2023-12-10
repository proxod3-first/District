from django.test import TestCase
from base.models import *
from datetime import datetime


# Tests for models


class TopicModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Topic.objects.create(name='C++')

    def test_name_label(self):
        topic = Topic.objects.get(id=1)
        field_label = topic._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_object_name_is_name_field(self):
        topic = Topic.objects.get(id=1)
        expected_object_name = f'{topic.name}'
        self.assertEquals(expected_object_name, str(topic))

    def test_verbose_name_plural(self):
        self.assertEquals(str(Topic._meta.verbose_name_plural), 'topics')

    def test_string_representation(self):
        topic = Topic.objects.get(id=1)
        expected_object_name = f'{topic.name}'
        self.assertEquals(expected_object_name, str(topic))
    

class RoomModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        host = User.objects.create(name="John Doe22", email="johndoe@example.com2", bio="Hello, I'm John!")
        topic = Topic.objects.create(name='test_topic')
        Room.objects.create(host=host, topic=topic, name='test_room', description='test_description')

    def test_host_label(self):
        room = Room.objects.get(id=1)
        field_label = room._meta.get_field('host').verbose_name
        self.assertEquals(field_label, 'host')

    def test_topic_label(self):
        room = Room.objects.get(id=1)
        field_label = room._meta.get_field('topic').verbose_name
        self.assertEquals(field_label, 'topic')

    def test_name_max_length(self):
        room = Room.objects.get(id=1)
        max_length = room._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_description_blank(self):
        room = Room.objects.get(id=1)
        blank = room._meta.get_field('description').blank
        self.assertTrue(blank)

    def test_participants_related_name(self):
        room = Room.objects.get(id=1)
        related_name = room._meta.get_field('participants').related_query_name()
        self.assertEquals(related_name, 'participants')

    def test_string_representation(self):
        room = Room.objects.get(id=1)
        self.assertEquals(str(room), room.name)
        


class UserModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        User.objects.create(name="John Doe", email="johndoe@example.com", bio="Hello, I'm John!")

    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_email_unique(self):
        user = User.objects.get(id=1)
        unique = user._meta.get_field('email').unique
        self.assertTrue(unique)

    def test_avatar_default(self):
        user = User.objects.get(id=1)
        default_avatar = user.avatar
        self.assertEqual(default_avatar, "avatar.svg")

    def test_username_field(self):
        self.assertEqual(User.USERNAME_FIELD, 'email')

    def test_required_fields(self):
        self.assertEqual(User.REQUIRED_FIELDS, [])



class MessageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.room = Room.objects.create(name='test_room')
        self.message1 = Message.objects.create(user=self.user, room=self.room, body='Test message 1')
        self.message2 = Message.objects.create(user=self.user, room=self.room, body='Test message 2')

    def test_message_str_method(self):
        self.assertEqual(str(self.message1), 'Test message 1')

    def test_message_ordering(self):
        messages = Message.objects.all()
        self.assertEqual(messages[0], self.message1)
        self.assertEqual(messages[1], self.message2)

    def test_create_message(self):
        new_message = Message.objects.create(user=self.user, room=self.room, body='New test message')
        self.assertEqual(new_message.body, 'New test message')

    def test_message_updated_timestamp(self):
        self.message1.body = 'Updated message'
        self.message1.save()
        self.assertGreater(self.message1.updated.hour, datetime.utcfromtimestamp(3).hour)