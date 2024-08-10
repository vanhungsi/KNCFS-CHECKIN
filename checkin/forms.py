from django.forms import ModelForm
from .models import Checkin

class CheckinForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(Checkin1Form, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget['class'] = 'form-control'

    class Meta:
        model = Checkin
        fields = "__all__"