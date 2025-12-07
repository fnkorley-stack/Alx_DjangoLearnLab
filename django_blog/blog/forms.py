from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag


class TagWidget(forms.TextInput):
    """Widget for entering comma-separated tags."""
    placeholder = "Enter tags separated by commas"

    def __init__(self, attrs=None):
        default_attrs = {'class': 'form-control', 'placeholder': self.placeholder}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=TagWidget(),
        help_text="Enter tags separated by commas."
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        post = super().save(commit=False)
        tags_input = self.cleaned_data.get('tags', '')

        if commit:
            post.save()

        # clear old tags if updating
        post.tags.clear()

        # add new tags
        for tag_name in [t.strip() for t in tags_input.split(',') if t.strip()]:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)

        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
