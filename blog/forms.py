from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'form-control',}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',}))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control',}))

  

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Name',
        }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }))

    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Comment',
    }))


    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']