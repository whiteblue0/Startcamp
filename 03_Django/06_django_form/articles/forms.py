from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'mytitle',
                'placeholder':'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content!',
                'row': 5,
                'cols':50,
            }
        )
    )
    # title = forms.CharField(max_length=20)
    # content = forms.Textarea(widget=forms)
