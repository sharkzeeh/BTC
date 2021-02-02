from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_news.png', upload_to='news_pics')

    def __str__(self):
        return self.title

    # resizing large images to 300 x 300
    def save(self, *args, **kwargs):
        '''
        resizes large images to (300, 300)
        '''
        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        '''
        finds a location to a specific post
        '''
        return reverse('post-detail', kwargs={'pk': self.pk })