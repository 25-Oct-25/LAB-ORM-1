from django.db import models

# Create your models here.
class Post(models.Model):
    '''
    title
    content
    is_published
    published_at    
    '''

    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(True)
    published_at = models.DateField(auto_now=True)  