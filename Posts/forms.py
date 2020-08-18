from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'name', 'body')


# class PostForm(forms.Form):
#     STATUS = (
#         ('draft', 'draft'),
#         ('published', 'published')
#     )

#     title = forms.CharField(max_length=100, required=True)
#     content = forms.CharField(widget=forms.Textarea)
#     cover_image = forms.ImageField()
#     status = forms.ChoiceField(choices=STATUS)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'cover_image', 'status')
