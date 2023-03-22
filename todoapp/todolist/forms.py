from django import forms
from .models import ToDo, Comment


class TodoForm(forms.ModelForm):
    """"""
    number = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control", "id": "number", "placeholder": "8(123)456-78-90"}))
    site = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "site", "placeholder": "example.ru"}))
    datatime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "date", "class": "form-control", "id": "datatime"}))
    comment = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "id": "comment"}))

    class Meta:
        model = ToDo
        fields = ('number', 'site', 'datatime', 'comment')


class UpdateCommentForm(forms.ModelForm):
   
    comment = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "id": "comment"}))

    class Meta:
        model = ToDo
        fields = ('comment',)


class CommentsFormModel(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Comment
        fields = ['text']