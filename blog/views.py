from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from .forms import CommentForm

def blog_list(request):
    """Lista svih objavljenih postova"""
    posts_list = Post.objects.filter(status='published')
    
    # Paginacija
    paginator = Paginator(posts_list, 6)  # 6 postova po strani
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/list.html', {'posts': posts})

def blog_detail(request, slug):
    """Detalji blog posta sa komentarima"""
    post = get_object_or_404(Post, slug=slug, status='published')
    
    # Povećaj broj pregleda
    post.views += 1
    post.save()
    
    # Komentari
    comments = post.comments.filter(approved=True)
    new_comment = None
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('blog_post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()
    
    return render(request, 'blog/detail.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    })