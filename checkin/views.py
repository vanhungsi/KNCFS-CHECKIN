# from django.shortcuts import render
from django.utils import timezone
from .models import Checkin
from django.views import generic
from .forms import CheckinForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.


class CheckinCreateView(generic.CreateView, SuccessMessageMixin):
    model = Checkin
    form_class = CheckinForm
    template_name = 'checkin-create.html'
    success_message = 'Cảm ơn bạn đã check-in thành công!'
    success_url = reverse_lazy('checkin:checkin-create')


class CheckinListView(generic.ListView, LoginRequiredMixin):
    model = Checkin
    template_name ='checkin-view.html'
    paginate_by = 50
    ordering = ['-checkin_time']


class CheckinUpdate(generic.UpdateView, LoginRequiredMixin):
    model = Checkin
    template_name = 'checkin-update.html'
    form_class = CheckinForm
    success_message = "Updated successfully!"
    success_url = reverse_lazy('checkin:checkin-view')


class CheckinDelete(generic.DeleteView, LoginRequiredMixin):
    model = Checkin
    template_name = 'checkin-delete.html'
    success_message = 'Deleted Successfully!'
    success_url = reverse_lazy('checkin:checkin-view')