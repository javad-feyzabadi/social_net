from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=2080)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural  = 'posts'
        db_table = 'post'

    def __str__(self):
        return self.title

class PostFile(models.Model):
    post = models.ForeignKey(to=Post,on_delete=models.CASCADE)
    file = models.FileField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'post file'
        verbose_name_plural  = 'posts file'
        db_table = 'post file'

    def __str__(self):
        return self.post

class Comment(models.Model):
    post = models.ForeignKey(to=Post,related_name='comments',on_delete=models.PROTECT)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural  = 'comments'

class Like(models.Model):
    post = models.ForeignKey(to=Post,related_name='likes',on_delete=models.PROTECT)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ='like'
        verbose_name_plural  = 'likes'
            
