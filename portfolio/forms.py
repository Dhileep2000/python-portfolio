from django.forms import ModelForm
from .models import *


class model_form(ModelForm):
    
    class Meta:
        model = model_port
        fields = "__all__"

        