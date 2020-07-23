from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse


from blog.models import BlogPost, Comment
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm, CommentForm
from account.models import Account
from django.views.generic import DetailView, ListView, View
from django.core.exceptions import ObjectDoesNotExist


def create_blog_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=request.user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()

    context['form'] = form

    return render(request, 'blog/create_blog.html', context)


def detail_blog_view(request, slug):

    context = {}
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'blog/detail_blog.html', context)


def edit_blog_view(request, slug):

    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    blog_post = get_object_or_404(BlogPost, slug=slug)
    if request.POST:
        form = UpdateBlogPostForm(
            request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj

    form = UpdateBlogPostForm(
        initial={
            "title": blog_post.title,
            "body": blog_post.body,
            "image": blog_post.image,
        }
    )
    context['form'] = form

    return render(request, 'blog/edit_blog.html', context)


def post_detail(request, slug):
    template_name = 'blog/comment.html'
    post = get_object_or_404(BlogPost, slug=slug)
    comment = post.img.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blogpost = post
            new_comment.save()

    else:

        comment_form = CommentForm()

    return render(request, template_name, {'post': post, 'comments': comment,

                                           'new_comment': new_comment, 'comment_form': comment_form})
