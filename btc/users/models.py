from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Adding profile pictures
class Profile(models.Model):
    # if we delete a USER -> delete the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # upload_to = directory that images get uploaded to when we upload a profile
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(default='default_profile.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} profile"


    # https://stackoverflow.com/questions/52351756/django-typeerror-save-got-an-unexpected-keyword-argument-force-insert/52351829
    def save(self, *args, **kwargs):
        '''
        resizes large images to (300, 300)
        '''
        super(self.__class__, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




