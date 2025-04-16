from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.http import HttpResponse
from .forms import CommentForm


"""
Create view for show all posts in database
"""
def post_list(request):
    try:
        posts = Post.objects.all().order_by("-created_at")
        return render(request, "blog/post_list.html", {"posts": posts})
    except:
        return render(request, "blog/post_list.html", {"posts": "there is no post"})


"""
View to dispaly a single post with its comments and comment form
"""
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.mehtod == "POST":
        form = CommentForm(request.post)
        if form.is_valid():
            commnet = form.save(commit=False)
            commnet.post = post
            commnet.save()
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = CommentForm()
    
    return render(request, "blog/post_detail.html", {
        "post": post,
        "form": form
    })