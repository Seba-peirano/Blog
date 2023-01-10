from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import(
    BlogHomePageView,
    about,index,login_request, register,logout, PostDetailView
    )
app_name="blog"

urlpatterns= [
    path("", BlogHomePageView.as_view(), name="home"),
    path("about", about, name="about" ),
    path("index", index, name="index" ),
    path('login', login_request, name="login"),
    path('register', register, name="register"),
    path('logout', logout, name='logout'), #hasta aca
     path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]