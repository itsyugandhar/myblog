from django.shortcuts import render,HttpResponse

from .models import Post,BlogComments
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def blogpage(request):

    allposts = Post.objects.all()
    print(allposts)
    context = {'allposts' : allposts}
    return render(request,'blog/blogpage.html',context)

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    # context = {'post':post}
    # return render(request,'blog/blogpost.html',context)

    post = Post.objects.get(slug=slug)
    comments = BlogComments.objects.filter(post=post, parent=None)
    replies = BlogComments.objects.filter(post=post).exclude(parent=None)
    
    replyDict = {}
    for reply in replies:
        if reply.parent.Sno not in replyDict:
            replyDict[reply.parent.Sno] = [reply]
        else:
            replyDict[reply.parent.Sno].append(reply)

    context = {
        'post': post,
        'comments': comments,
        'replyDict': replyDict,
        'user': request.user
    }
    return render(request, 'blog/blogpost.html', context)

from django.shortcuts import redirect
from .models import BlogComments, Post
from django.contrib import messages

def postComment(request):
    if request.method == "POST":
        comment = request.POST['comment']
        user = request.user
        postSno = request.POST['postSno']
        post = Post.objects.get(Sno=postSno)
        parentSno = request.POST.get('parentSno')
        parent = None if parentSno == "" else BlogComments.objects.get(Sno=parentSno)

        new_comment = BlogComments(comment=comment, user=user, post=post, parent=parent)
        new_comment.save()
        messages.success(request, "Your comment has been posted successfully!")
    return redirect(f"/blog/{post.slug}")



@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.username  # author = username from logged-in user
            post.save()
            messages.success(request, "Your blog post has been created!")
            return redirect('blogpage')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog.html', {'form': form})

