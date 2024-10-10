from django.forms import ModelForm
from .models import GenericModel

class GenericModelForm(ModelForm):
    class Meta:
        model = GenericModel
        fields = [
            'title',
            'description',
            'type',
            'exceptional'
        ]