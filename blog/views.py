from django.views import generic
from .models import Post
from django.utils import timezone

class IndexView(generic.TemplateView):
    template_name = "index.html"

class BlogListView(generic.ListView):
    model = Post
    template_name = 'blog_list.html'
    context_object_name = 'blog_list'

    paginate_by = 5

    def get_queryset(self):
        blogs = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return blogs

class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blog_detail.html'