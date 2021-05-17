from django import forms

class MovieForm(forms.Form):
    s = forms.CharField(max_length=1)
    w = forms.CharField(max_length=1)
    n = forms.CharField(max_length=1)
    e = forms.CharField(max_length=1)
    s_w = forms.CharField(max_length=1)
    s_e = forms.CharField(max_length=1)
    n_w = forms.CharField(max_length=1)
    n_e = forms.CharField(max_length=1)
    c = forms.CharField(max_length=1)
