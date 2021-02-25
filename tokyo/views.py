from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Profile,Post
from django.views.generic import View
# Create your views here.

def index(request):
    profile = Profile.objects.get(id=1)
    post=Post.objects.all().order_by('-id')
    return render(request, 'tokyo/index.html', {'profile': profile, 'post':post})


# class IndexView (TemplateView):
#     template_name = "tokyo/index.html"

class AboutView (TemplateView):
    template_name = "tokyo/about.html"

class ExperiencesView (TemplateView):
    template_name = "tokyo/experiences.html"

class WorksView (TemplateView):
    template_name = "tokyo/works.html"   

class SkillsView (TemplateView):
    template_name = "tokyo/skills.html"

class ContactsView (TemplateView):
    template_name = "tokyo/contacts.html"

# def detail(request, post_id):
#    post = get_object_or_404(Post, id=post_id)
#    comments = Comment.objects.filter(post=post).order_by('-created_at')
#    liked = False
#    if post.like.filter(id=request.user.id).exists():
#       liked = True
#    if request.method == "POST":
#        form = CmtForm(request.POST or None)
#        if form.is_valid():
#            text = request.POST.get('text')
#            comment = Comment.objects.create(post=post, user=request.user, text=text)
#            comment.save()
#    else:
#          form = CmtForm()
#    context = {
#          'post': post,
#          'comments': comments,
#          'form': form,
#          'liked': liked
#           }    
#    if request.is_ajax():
#          html = render_to_string('okayama/comment.html', context, request=request )
#          return JsonResponse({'form': html}) 
#    return render(request, 'okayama/detail.html', {'post': post, 'form': form, 'comments': comments, 'liked': liked})

