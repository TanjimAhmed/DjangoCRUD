from django.forms import ModelForm
from .models import *

class blogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
