# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User 

class Profile(models.Model):
    name = models.CharField('名前', max_length=35)
    education = models.CharField('教育', max_length=35)
    github= models.CharField('GitHub', max_length=35)
    facebook= models.CharField('facebook', max_length=35)
    blog= models.CharField('blog', max_length=35)
    mail= models.CharField('mail', max_length=35)
    mobile = models.CharField('携帯', max_length=35)
    def __str__(self):
        return self.name

class Tag(models.Model):
 tag = models.CharField('タグ名', max_length=50)
 def __str__(self):
   return self.tag

class Post(models.Model):
   title = models.CharField('タイトル', max_length=35)
   text = models.TextField('本文')
   image = models.ImageField('画像', upload_to = 'images', blank=True)
   created_at = models.DateTimeField('投稿日', default=timezone.now)
   tag = models.ForeignKey(Tag, verbose_name = 'タグ', on_delete=models.PROTECT)
   user = models.ForeignKey(User, on_delete=models.CASCADE)   
   like = models.ManyToManyField(User, related_name='like', blank=True)
   def __str__(self):
       return self.title








