from rest_framework.serializers import ModelSerializer
from base.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        
        
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'