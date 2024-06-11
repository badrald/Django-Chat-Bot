from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



class ChatGroup(models.Model):
    user=models.ForeignKey(User,related_name="chat_group_user",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    members = models.ManyToManyField(User, related_name="chat_groups")

    def save(self, *args, **kwargs):
        # Auto-generate slug based on the name if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    



class ChatMessage(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user:{self.user} - Chat_Group: {self.group}'
