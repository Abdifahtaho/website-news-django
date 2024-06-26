from asyncio import log
from multiprocessing import context
from newsApp.forms import CategoryForm
from newsApp.forms import PostForm
from newsApp.forms import ContactForm
from django.shortcuts import redirect, render
from django.db.models import Count
from newsApp.models import contact
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


from newsApp.models import Post, category

# Create your views here.

@login_required(login_url="/users/login/")
def home(request):
    ps=Post.objects.order_by('-id')
    context={"post":ps}
    return render(request,'index.html',context=context)


def base(request):

    return render(request,'base.html')

@login_required(login_url="/users/login/")
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/category_form')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

@login_required(login_url="/users/login/")
def add_post(request):
    if request.method == 'POST':
       
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


@login_required(login_url="/users/login/")
def health(request):
    # Retrieve the 'Health' category
    health_posts = Post.objects.filter(category__name='health')
    return render(request, 'health.html', {'health_posts': health_posts})

@login_required(login_url="/users/login/")
def bussiness(request):
    # Retrieve the 'Health' category
    bussiness_posts = Post.objects.filter(category__name='bussiness')
    return render(request, 'bussiness.html', {'bussiness_posts': bussiness_posts})

@login_required(login_url="/users/login/")
def politacal(request):
    # Retrieve the 'Health' category
    politacal_posts = Post.objects.filter(category__name='politacal')
    return render(request, 'politacal.html', {'politacal_posts': politacal_posts})

@login_required(login_url="/users/login/")
def football(request):
    # Retrieve the 'Health' category
    football_posts = Post.objects.filter(category__name='football')
    return render(request, 'football.html', {'football_posts': football_posts})

@login_required(login_url="/users/login/")
def world_news(request):
    # Retrieve the 'Health' category
    world_news_posts = Post.objects.filter(category__name='world-news')
    return render(request, 'world_news.html', {'world_news_posts': world_news_posts})

@login_required(login_url="/users/login/")
def update(request,pk):
    obj1=Post.objects.get(pk=pk)
    form=PostForm(instance=obj1)
    if request.method=='POST':
        form=PostForm(request.POST ,instance=obj1)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'update.html',{'for':form})
    
def delete(request,pk):
    obj2=Post.objects.get(pk=pk)
    obj2.delete()
    return redirect('home')


@login_required(login_url="/users/login/")
def c_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect to a success page or list view
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

@login_required(login_url="/users/login/")
def dis_contact(request):
    contacts = contact.objects.all()
    return render(request, 'dis_contact.html', {'contacts': contacts})



