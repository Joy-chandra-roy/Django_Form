from django import forms

class studentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your address', 'rows': 3}))