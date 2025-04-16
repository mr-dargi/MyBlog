from django import forms
from .models import Comment


"""
A form for submitting a comment under post
"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "text"]