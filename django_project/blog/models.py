from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user deleted all his posts get deleted

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    # This is needed so that the CreatePostView knows exactly where to go after it's done
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
