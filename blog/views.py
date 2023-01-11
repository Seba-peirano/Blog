from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate
from .forms import RegistroUsuarioForm

class BlogHomePageView(TemplateView):
    template_name= "blog/index.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["posts"]= Post.postobjects.all()
        return context

def index(request):
    return render(request, "blog/index.html")
def NewPost(request):
    return render(request, "blog/new-post.html")

def about(request):
    return render(request, "about.html") 

def login_request (request):
    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")

            user= authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request,"login.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"login.html", {"mensaje":"Error, datos incorrectos."})
        else:
            return render(request,"login.html", {"mensaje":"Error, formulario erroneo."})
    form= AuthenticationForm()
    return render (request,"login.html",{"form":form} )

def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            #aca se podria loguear el usuario, con authenticate y login... pero no lo hago
            return render(request, "register.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "register.html", {"form":form, "mensaje":"Error al crear el usuario"})
        
    else:
        form=RegistroUsuarioForm()
    return render(request, "register.html", {"form":form})

def logout(request):
    return render(request, "logout.html")

class PostDetailView (DetailView):
    model= Post
    template_name='blog/post-detail.html'
    context_object_name='post'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        post= Post.objects.filter(slug=self.kwargs.get ('slug'))
        return context 