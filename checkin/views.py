# from django.shortcuts import render
from .models import Checkin
from django.views import generic
from .forms import CheckinForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# from django.http import HttpResponseRedirect, Http404


# Create your views here.


class CheckinCreateView(generic.CreateView, SuccessMessageMixin):
    model = Checkin
    form_class = CheckinForm
    template_name = 'checkin-create.html'
    success_message = 'Cảm ơn bạn đã check-in thành công!'
    success_url = reverse_lazy('checkin:checkin-create')

