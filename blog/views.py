from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Comment
from django.http import HttpResponse
from .forms import CommentForm


"""
Create view for show all posts in database
"""
def post_list(request):
    posts = Post.objects.all().order_by("-create_at")
    paginator = Paginator(posts, 5)
    # Get current page number from GET parameter (?page=2)
    page_number = request.GET.get("page")
    # Get the page object
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/post_list.html", {"page_obj": page_obj})


"""
View to dispaly a single post with its comments and comment form
"""
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            commnet = form.save(commit=False)
            commnet.post = post
            commnet.save()
            return redirect("blog:detail", pk=post.pk)
    else:
        form = CommentForm()
    
    return render(request, "blog/post_detail.html", {
        "post": post,
        "form": form
    })