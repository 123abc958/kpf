from django.contrib import admin

# Register your models here.
from .models import Profile,Tag,Post
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Post)