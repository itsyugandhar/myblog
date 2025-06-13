
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from  blog.models import Post
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    # return HttpResponse('This is home page')
    return render(request,'home/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        # print(name, email, password,content)
        if len(name) < 3 or len(email)< 7 or len(phone) < 6 or len(content) < 10:
            messages.error(request,"Please fill the form properly")
        else:
            contact = Contact(name= name,email  = email ,phone= phone,content = content)
            contact.save()
            messages.success(request,"your responce has been submitted..!")


    return render(request,'home/contact.html')
    # return HttpResponse('This is contact page')

def about(request):
    return render(request,'home/about.html')
    # return HttpResponse('This is about page')


def search(request):
    query = request.GET['query']
    if len(query) >78:
        allposts = Post.objects.none()
    else:
        allposts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(content__icontains=query)
        )

    if allposts.count() == 0:
        messages.warning(request,"No searh results found ..Please refine your query")

    else:
        messages.success(request,"We have found your results")



    output = {'allposts' : allposts}

    return render(request,'home/search.html',output)

def blogsignup(request):
    if request.method == "POST":

        # parameters 
        username = request.POST['username']
        inputfname = request.POST['inputfname']
        inputlname = request.POST['inputlname']
        inputemail = request.POST['inputemail']
        inputpass1 = request.POST['inputpass1']
        inputpass2 = request.POST['inputpass2']



        if len(username) > 10:
            messages.error(request,"Your user name must be below 10 characters")
            return redirect('home')
        
        if not username.islanum():
            messages.error(request,"Your user name should only contains characters")
        
        if(inputpass1 != inputpass2):
            messages.error(request,"Password do not match ..please check ...!")
            return redirect('home')


# code for creating user
        myuser = User.objects.create_user(username, inputemail, inputpass1)
        myuser.first_name = inputfname
        myuser.last_name = inputlname
        myuser.save()
        messages.success(request,"Your account has  been created successfully")
        return redirect('home')
    else:
        return HttpResponse("Error  -  Please try APOST")
    
def bloglogin(request):
    if request.method == 'POST':
        # parameters for post
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']



        user = authenticate(username =loginusername, password = loginpassword)
        if user is None:
            messages.error(request,"Invalid credentials..!,please check")
            return redirect('home')
        else:
            login(request,user)
            messages.success(request," hey  !!!! ...suessfully logged in")
            return redirect('home')
    return HttpResponse("404 - Not found")

def bloglogout(request):
    logout(request)
    messages.success(request,"successfully  logged out...!")
    return redirect('home')



@login_required
def profile(request):
    return render(request, 'home/profile.html', {'user': request.user})

def blog_home(request):
    posts = Post.objects.all().order_by('-timeStamp')[:2]  # Only latest 2
    return render(request, 'blog/home.html', {'posts': posts})

def user_profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)
    return render(request, 'blog/profile.html', {'user_profile': user, 'posts': posts})










