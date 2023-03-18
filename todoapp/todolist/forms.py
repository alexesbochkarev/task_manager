from django import forms
from .models import ToDo


class TodoForm(forms.ModelForm):
    

    number = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control", "id": "number", "placeholder": "8(123)456-78-90"}))
    site = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "site", "placeholder": "example.ru"}))
    datatime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control", "id": "datatime"}))
    comment = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "id": "comment"}))

    class Meta:
        model = ToDo
        fields = ('number', 'site', 'datatime', 'comment')
