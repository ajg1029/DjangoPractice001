from django import forms
from .models import Article

'''
class ArticleForm(forms.Form):
    REGION_A = 'sl'
    REGION_B = 'bs'
    REGION_C = 'gj'
    REGION_CHOICES = [
        (REGION_A, '서울'),
        (REGION_B, '부산'),
        (REGION_C, '광주')
    ]
    
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select)

'''
    
class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        # fields = ('title', 'content')
        # fields = ['title', 'content']
        fields = '__all__'
        # exclude = ('title',)