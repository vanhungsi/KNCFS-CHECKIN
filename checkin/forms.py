from django.forms import ModelForm
from django import forms
from .models import Checkin


class CheckinForm(ModelForm):
    signature = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    def __init__(self, *args, **kwargs):
        super(CheckinForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Checkin
        fields = "__all__"