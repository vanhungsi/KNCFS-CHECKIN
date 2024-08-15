from django.forms import ModelForm
from django import forms
from .models import Factory


class FactoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FactoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Factory
        fields = "__all__"