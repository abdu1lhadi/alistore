from django import template
from blog.models import Post, Comment, Top5

register = template.Library()
@register.inclusion_tag('blog/latest_posts.html')
def latest_posts():
    context = {
        'l_posts': Post.objects.all()[0:10]
    }
    return context

@register.inclusion_tag('blog/latest_comments.html')
def latest_comments():
    context = {
        'l_Top5': Top5.objects.all()[0:7]
    }
    return context