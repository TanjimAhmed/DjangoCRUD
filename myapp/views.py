# importing render and redirect
from django.shortcuts import render, redirect
#importing models form models files
from .models import *
# importing jango httpresponse
from django.http import HttpResponse
#importing the forms files
from .forms import *

# Create your views here.
def home(request):
    #importing blogs objects from Blog model
    blog = Blog.objects.all()
    #importing authors objects from Author model
    authors = Author.objects.all()
    # Count method to get the total data
    total_blog = blog.count()
    # dictionary to pass the data
    context = {'posts':blog,
    'authors':authors,
    'total_blog': total_blog}
    # return and render to the urls
    return render(request, 'myapp/index.html', context)

def authorPage(request, pk_id):
    # using primary key to get the data form one user
    author = Author.objects.get(id=pk_id)
    context={'author': author,}
    return render(request, 'myapp/author.html', context)

def createPage(request, author_id):
    author = Author.objects.get(id=author_id)
    # initial is user to prefill the form
    form = blogForm(initial={'author':author})
    # if the request is post
    if request.method == 'POST':
        # set the data to the form
        form = blogForm(request.POST)
        # check the data if valid
        if form.is_valid():
            # save the data
            form.save()
            # redirect to the home page
            return redirect('/')


    context={'form': form,}
    return render(request, 'myapp/create.html', context)
    
def about(request):
    return render(request, 'myapp/about.html')