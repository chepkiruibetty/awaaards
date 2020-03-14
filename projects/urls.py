from django.urls import path
from . import views
from .views import PostListView,PostDetailView 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'), 
path('', PostListView.as_view(), name='home'),
# path('profile/', views.profile, name='profile'),
# path('update/profile', views.updateprofile, name='update'),
path('post/new/', views.post_new, name='post_new'),
path('search/',views.search_results,name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
