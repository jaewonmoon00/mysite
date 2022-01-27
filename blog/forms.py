from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # By default, Django will generate a form dynamically from all fields of the model
        fields = ('name', 'email', 'body')