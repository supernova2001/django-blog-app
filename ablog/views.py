from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
from .forms import PostForm
# Create your views here.

#def Home(request):
    #return render(request,'index.html',{})

class Home(ListView):
    model=Post
    template_name='index.html'

class Detailview(DetailView):
    model=Post 
    template_name='details.html'

class AddPost(CreateView):
    model=Post 
    form_class=PostForm 
    template_name='addpost.html'

