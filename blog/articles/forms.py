from django import forms

from .models import Article

class ArticleModelForm(forms.ModelForm):
    """ Article model form """
    class Meta:
        model = Article
        fields = ['title', 'text', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }
