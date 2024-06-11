from django.contrib import admin
from .models import ChatMessage,ChatGroup
# Register your models here.


admin.site.register(ChatMessage)
admin.site.register(ChatGroup)