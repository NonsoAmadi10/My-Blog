from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 1


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    comments = post.comments.filter(active=True)

    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post

            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post,
                                                'comments': comments,
                                                'new_comment': new_comment,
                                                'comment_form': comment_form

                                                })


class CreatePostView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = PostForm
    success_url = reverse_lazy('home')
    template_name = 'create_post.html'
    success_message = 'Your post has been published.'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

# @login_required
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # new_post = form.save(commit=False)
#             # #new_post.cover_image = request.FILES['cover_image'].name
#             # new_post.author = request.user

#             form.save()

#             messages.success(request, 'Your Post Has Been Saved!')
#             return redirect('home')
#         else:
#             messages.error(request, 'Please Check Your Input Fields')
#             return ('new_post')
#     else:
#         form = PostForm()
#         return render(request, 'create_post.html', {'form': form})
