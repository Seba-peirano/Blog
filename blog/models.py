from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Category(models.Model):
    name=models.CharField(max_length= 100)
    def __str__(self):
        return self.name

class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")
    OPTIONS= (("draft", "Draft"),("published","Published"))
    category=models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title=models.CharField(max_length=255)
    excerpt=models.TextField()
    content=RichTextField()
    slug=models.SlugField(max_length=250, unique_for_date="published", null=False, unique=True)
    published=models.DateTimeField(default=timezone.now)
    author=models.CharField(max_length=30)
    #author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    status= models.CharField(max_length=10, choices=OPTIONS , default="draft")
    #imagen=models.ImageField(upload_to="images", null=True)
    objects= models.Manager()
    postobjects=PostObjects()
    

    class Meta:
        ordering= ("-published",)
    def __str__(self) :
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name=models.CharField(max_length=80)
    email=models.EmailField()
    content=models.TextField()
    publish=models.DateTimeField(auto_now_add=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering= ("publish",)
    def __str__(self) :
        return f"Comment by {self.name}"