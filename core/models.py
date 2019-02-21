from django.db import models
from django.contrib.auth import get_user_model

import uuid
User = get_user_model()

class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    upddated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class ChatSession(TimeStamp):
    
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return str(self.uuid)

class ChatSessionMessage(TimeStamp):
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)    
    chat_session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.PROTECT)
    message = models.TextField()

    def __str__(self):
        return self.message
    
class ChatSessionMember(TimeStamp):
    
  user = models.ForeignKey(User, related_name='members', on_delete=models.PROTECT)
  chat_session =  models.ForeignKey(ChatSession, 
    related_name='member_sessions', on_delete=models.PROTECT)

  class Meta:
      ordering = ['-id']

  def __str__(self):
    return self.user.get_full_name()


