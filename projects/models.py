from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q

# Create your models here

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title= models.CharField(max_length=50)
    desc= models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='projects/')
    link = models.CharField(max_length=70)
    technologies = models.CharField(max_length=100)


    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

        
    def search(self,searchterm):
        search = Post.objects.filter(Q(title__icontains=searchterm)|Q(description__icontains=searchterm)|Q(country__icontains=searchterm))
        return search



    def get_absolute_url(self): 
        return reverse('post_detail', args=[str(self.id)])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_pics/')
    bio = models.TextField(default="Hello there!")
    email = models.CharField(blank = True, max_length = 100)

    def __str__(self):
        return self.image

    def save_profile(self):
        self.save()
    

    

