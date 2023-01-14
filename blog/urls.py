from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from blog.views import(
    BlogHomePageView,
    about,Login_request, register,logout, PostDetailView,NewPost,AllPost,HomePageView, FormPost,Construccion
    )

app_name="blog"

urlpatterns= [
  
    path('',HomePageView, name='home'),
    path("about", about, name="about" ),
    
    path('login', Login_request, name="login"),
    path('newpost', NewPost, name="newpost"),
    path('construccion', Construccion, name="construccion"),
    path('allpost', BlogHomePageView.as_view(), name="allpost"),
    path('register', register, name="register"),
    path('logout', LogoutView.as_view(), name='logout'), #hasta aca
    path('new-post', login_required(FormPost), name='new-post'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )