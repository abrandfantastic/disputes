from django.views import generic

#from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.utils import timezone
from . models import Post



#def blog(request):
 #   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
  #  return render(request, 'blog.html', {'posts': posts})

#def blog(request):
#    return render(request, 'blog.html')

#def post_detail(request, pk):
 #   post = get_object_or_404(Post, pk=pk)
  #  return render(request, 'post_detail.html', {'post': post})

class BlogListView(ListView):
    model = Post
    template_name = "blog.html"
    ordering = ['-published_date']

    def __str__(self):
        return self.title

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    def __str__(self):
        return self.title