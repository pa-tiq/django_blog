from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.contrib.auth.models import User


class AboutView(TemplateView):
    template_name = "about.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # __lte = less or equal than
        # this query shows Posts with published_date <= now() ordered descending
        # return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return Post.objects.raw(
            """
            SELECT * FROM blog_post 
            WHERE published_date <= CURRENT_TIMESTAMP 
            ORDER BY published_date DESC
            """
        )


class PostDetailView(DetailView):
    model = Post


#class PostCreateView(LoginRequiredMixin, CreateView):
#    login_url = "login/"
#    redirect_field_name = "blog/post_detail.html"
#    form_class = PostForm
#    model = Post
#    
#    def get(self, request):
#        form = self.form_class(initial=self.initial)
#        return render(request, 'blog/post_form.html',{'form':form})
#
#    
#    def post(self, request):
#        form = self.form_class(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.save()
#            return redirect('blog:post_detail',pk=post.pk)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "login/"
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post


class PostRemoveView(LoginRequiredMixin, DeleteView):
    model = Post
    # reverse_lazy waits until the delete is done to redirect you
    success_url = reverse_lazy("blog:post_list")


class DraftListView(LoginRequiredMixin, ListView):
    template_name = "post_draft_list.html"
    context_object_name = 'drafts'
    login_url = "login/"
    model = Post
    
    def get_queryset(self):
        # return Post.objects.filter(published_date__isnull=True).order_by('create_date')
        return Post.objects.raw(
            """
            SELECT * FROM blog_post 
            WHERE published_date IS NULL 
            ORDER BY create_date ASC
            """
        )
        
@login_required        
def create_post(request):
    if request.method == 'POST':   
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html',{'form':form})

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':   
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)
