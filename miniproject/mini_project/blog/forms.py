from django import forms
from .models import Post, Category


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('title', 'body')
        exclude = ('user', 'slug', 'updated', 'created')


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'slug', 'updated', 'created')


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)

