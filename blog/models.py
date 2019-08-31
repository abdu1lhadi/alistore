from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    image_project = models.ImageField(default='default.jpg', upload_to='post_co')
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     if img.width > 800 or img.height > 800:
    #         output_size = (800, 800)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])

    class Meta:
        ordering = ('-post_date', )

class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الاكتروني')
    body = models.TextField(verbose_name='التعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    def __str__(self):
        return 'علق {} على {}.'.format(self.name, self.post)
    
    class Meta:
        ordering = ('-comment_date', )

class Top5(models.Model):
    image_top = models.ImageField(default='default.jpg', upload_to='top_5')
    title = models.CharField(max_length=100)
    old_prais = models.CharField(max_length=100)
    new_prais = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('topdetail', args=[self.pk])

