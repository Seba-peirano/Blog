from django.urls import path
from .views import(
    BlogHomePageView,
    about,index,login_request, register
)
app_name="blog"

urlpatterns= [
    path("", BlogHomePageView.as_view(), name="home"),
    path("about", about, name="about" ),
    path("index", index, name="index" ),
    path('login', login_request, name="login"),
    path('register', register, name="register"),
]