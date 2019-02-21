from django.test import TestCase
from model_mommy import mommy
from core.models import ChatSession, ChatSessionMessage
from django.contrib.auth import get_user_model
# Create your tests here.
class TestChatModel(TestCase):
    def setUp(self):
        self.user = mommy.make(get_user_model())
        self.chat_session = mommy.make(ChatSession, owner__email='email@email.com')
        self.chat_message = mommy.make(ChatSessionMessage, _quantity=10,
                    chat_session=self.chat_session, user=self.user)
    def test_chat_session(self):
        """chat session"""
        self.assertTrue(ChatSession.objects.exists())

    def test_chat_has_message(self):
        """chat has owner"""
        self.assertIsInstance(self.chat_session.owner, get_user_model())
        
    def test_chat_has_email(self):
        """chat has email"""
        self.assertEqual(self.chat_session.owner.email, 'email@email.com')

    def test_chat_session_has_message(self):
        """chat has messages"""
        messages = ChatSessionMessage.objects.filter(chat_session__uuid=self.chat_session.uuid)
        self.assertEquals(messages.count(), 10)
        
    
    
