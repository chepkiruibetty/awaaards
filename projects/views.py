from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .forms import PostForm,ProfileForm
from .models import *

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'projects/index.html'


class PostDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'

    
# def profile(request):
#     current_user = request.user
#     profile = Profile.objects.filter(user=current_user).first()
#     posts = request.user.post_set.all()

#     return render(request, 'projects/profile.html', locals())

# def updateprofile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = ProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             add = form.save(commit=False)
#             add.user = current_user
#             add.save()
#             return redirect('profile')
#     else:
#         form = ProfileForm()
#     return render(request, 'projects/profile_update.html',{"form":form })


def post_new(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('home')
    else:
        form = PostForm()
    return render(request, 'projects/post_new.html', {"form": form})

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search(search_term)
        message = f"{search_term}"

        return render(request, 'projects/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'projects/search.html',{"message":message})





