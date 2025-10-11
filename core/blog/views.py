from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

# Function Base View show a template
'''
def indexView(request):
    """
    a function based view to show index page
    """
    name = 'marzya'
    context = {'name':name}
    return render(request,"index.html",context)
'''

class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'marzya'
        context['posts'] = Post.objects.all()
        return context
    
''' FBV for redirect

from django.shortcuts import redirect
def RedirectToMaktab(request):
    return redirect('https://maktabkhooneh.com')

'''
class RedirectToMaktab(RedirectView):
    url ='https://maktabkhooneh.org/'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    

class PostList(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.filter(status=False)
        return posts
    
