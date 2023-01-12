from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.views import LogoutView
from blog.views import(
    BlogHomePageView,
    about,login_request, register,logout, PostDetailView,NewPost,AllPost,HomePageView, FormPost
    )
app_name="blog"

urlpatterns= [
  
    path('',HomePageView, name='home'),
    path("about", about, name="about" ),
    
    path('login', login_request, name="login"),
    path('newpost', NewPost, name="newpost"),
    path('allpost', BlogHomePageView.as_view(), name="allpost"),
    path('register', register, name="register"),
    path('logout', logout, name='logout'), #hasta aca
    path('new-post', FormPost, name='new-post'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )