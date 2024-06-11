from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import os


def upload_pics(instance, filename):
    profile_folder = os.path.join(settings.MEDIA_ROOT, "Profiles")
    if not os.path.exists(profile_folder):
        os.makedirs(profile_folder)

    # Safely extract the file extension
    ext = filename.split(".")[-1]
    new_file_name = f"Profiles/{instance.id}.{ext}"
    new_filePath = os.path.join(settings.MEDIA_ROOT, new_file_name)

    if os.path.exists(new_filePath):
        os.remove(new_filePath)

    return new_file_name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_photo = models.ImageField(upload_to=upload_pics, null=True, blank=True)

    def __str__(self):
        if self.user.first_name == "" or self.user.first_name == None:
            return self.user.username
        return self.user.first_name + " " + self.user.last_name



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
