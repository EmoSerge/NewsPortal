from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'authorP',
            'title',
            #'category_type',#
            'post_category',
            'text'
        ]
