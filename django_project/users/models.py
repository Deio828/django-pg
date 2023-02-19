from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    """
    In this class we will extend the user model and add more new feilds to it which is the Profile Pic.
    """
    # When user is deleted delete profile but not the vise versa
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one to one relation with the user
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self) -> str:
        return f"{self.user.username} Profile"
    
    def save(self):
        super().save()
        image = Image.open(self.image.path)
        image.thumbnail((300, 300))
        image.save(self.image.path)
