from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import ChatSessionMessage, ChatSessionMember
User =  get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class ChatSessionMessageSerializer(serializers.ModelSerializer):
    username = serializers.RelatedField(source='user', read_only=True)
    class Meta:
        model = ChatSessionMessage
        fields = ('id', 'username', 'message')
    
class ChatSessionMemberSerializer(serializers.ModelSerializer):
    chat_session = serializers.RelatedField(source='chat_session', queryset=ChatSessionMember.objects.all())
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    class Meta:
        model = ChatSessionMember
        fields = ('id', 'full_name', 'chat_session')
