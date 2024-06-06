from asyncio import log
from multiprocessing import context
from pyexpat.errors import messages
from newsApp.forms import CategoryForm
from newsApp.forms import PostForm
from newsApp.forms import ContactForm
from django.shortcuts import redirect, render
from django.db.models import Count
from newsApp.models import contact
from newsApp.forms import CreateUserForm
from newsApp.forms import LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from newsApp.models import Post, category

# Create your views here.

@login_required(login_url='/login')
def home(request):
    ps=Post.objects.order_by('-id')
    context={"post":ps}
    return render(request,'index.html',context=context)

def base(request):

    return render(request,'base.html')


def add_category(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/category_form')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/posts/add')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})



def health(request):
    
    health_posts = Post.objects.filter(category__name='health')
    return render(request, 'health.html', {'health_posts': health_posts})

def bussiness(request):
    
    bussiness_posts = Post.objects.filter(category__name='bussiness')
    return render(request, 'bussiness.html', {'bussiness_posts': bussiness_posts})

def politacal(request):
    
    politacal_posts = Post.objects.filter(category__name='politacal')
    return render(request, 'politacal.html', {'politacal_posts': politacal_posts})


def football(request):
   
    football_posts = Post.objects.filter(category__name='football')
    return render(request, 'football.html', {'football_posts': football_posts})
@login_required
def world_news(request):
    
    world_news_posts = Post.objects.filter(category__name='world-news')
    return render(request, 'world_news.html', {'world_news_posts': world_news_posts})


def update(request,pk):
    obj1=Post.objects.get(pk=pk)
    form=PostForm(instance=obj1)
    if request.method=='POST':
        form=PostForm(request.POST ,instance=obj1)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request,'update.html',{'for':form})
    
def delete(request,pk):
    obj2=Post.objects.get(pk=pk)
    obj2.delete()
    return redirect('/home')



def c_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')  
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def dis_contact(request):
    contacts = contact.objects.all()
    return render(request, 'dis_contact.html', {'contacts': contacts})


def userreg(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        uform = CreateUserForm(request.POST)
        if uform.is_valid():
            username = uform.cleaned_data.get('username')
            email = uform.cleaned_data.get('email')
            password = uform.cleaned_data.get('password')
            
            # Validate password length
            if len(password) < 3:
                messages.error(request, 'Password must be at least 3 characters long')
                return redirect('userreg')
            
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Error, username already exists. Please use another.')
                return redirect('userreg')
            
            # Create new user
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            
            messages.success(request, 'User successfully created. You can now log in.')
            return redirect('login')
    else:
        uform = CreateUserForm()
    
    context = {'userreg': uform}
    return render(request, 'userreg.html', context)

def login(request):
    formss = LoginForm()
    if request.method == 'POST': 
        formss = LoginForm(request, data=request.POST)
        if formss.is_valid():
            username = formss.cleaned_data.get('username')
            password = formss.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            
    context = {'loginform': formss}  
    return render(request, 'login.html', context) 


def logout(request):
    
    return redirect('login')

