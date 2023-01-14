from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate
from .forms import RegistroUsuarioForm, PostFormulario
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



class BlogHomePageView(TemplateView):
    template_name= "blog/allpost.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["posts"]= Post.postobjects.all()
        return context

@login_required
def NewPost(request):
    data={
        'form':PostFormulario()
    }

    if request.method=="POST":
        formulario_post=PostFormulario(data=request.POST)
        if formulario_post.is_valid():
            formulario_post.save()
            return render(request,"blog/inicio.html")
        else:
            formulario=PostFormulario()
        return render(request, "blog/new-post.html", {"form":formulario})
    else:
        formulario=PostFormulario()
    return render(request, "blog/new-post.html", {"form":formulario})

def AllPost(request):
    return render(request, "blog/allpost.html")

def about(request):
    return render(request, "blog/about.html") 

def Construccion(request):
    return render(request, "blog/construccion.html") 

def Login_request (request):
    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")

            user= authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request,"blog/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"blog/login.html", {"mensaje":"Error, datos incorrectos."})
        else:
            return render(request,"blog/login.html", {"mensaje":"Error, formulario erroneo."})
    else:
        form= AuthenticationForm()
    return render (request,"blog/login.html",{"form":form} )

def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            #aca se podria loguear el usuario, con authenticate y login... pero no lo hago
            return render(request, "blog/register.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "blog/register.html", {"form":form, "mensaje":"Error al crear el usuario"})
        
    else:
        form=RegistroUsuarioForm()
    return render(request, "blog/register.html", {"form":form})

@login_required
def logout(request):
    return render(request, "blog/logout.html")

class PostDetailView (DetailView):
    model= Post
    template_name='blog/postdetail.html'
    context_object_name='post'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        post= Post.objects.filter(slug=self.kwargs.get ('slug'))
        return context 
def HomePageView(request):
    return render(request, 'blog/inicio.html') 

@login_required
def FormPost (request):
    if request.method=="POST":
        formulario_post=PostFormulario(request.POST)
              
        if formulario_post.is_valid():
            informacion=formulario_post.cleaned_data
            formulario1=Post(title=informacion["title"], excerpt=informacion["excerpt"])
            formulario1.save()
            return render(request,"blog/inicio.html")
        else:
            formulario=PostFormulario()
        return render(request, "blog/new-post.html", {"form":formulario})
    else:
        formulario=PostFormulario()
    return render(request, "blog/new-post.html", {"form":formulario})
