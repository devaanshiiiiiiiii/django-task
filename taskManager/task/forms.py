from django import forms
from .models import user,Task

class userForm(forms.ModelForm):
    class meta:
        model = user
        data = ['name','email','contact','id']
    class beta:
        model=Task
        data=['title','description','usserAssigned']
