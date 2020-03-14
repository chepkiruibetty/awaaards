from django.contrib import admin
from .models import Post, Profile
admin.site.site_header='Betty Developer'

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)

