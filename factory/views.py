# from django.shortcuts import render
from django.utils import timezone
from .models import Factory
from django.views import generic
from .forms import FactoryForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages


# Create your views here.


class FactoryCreateView(generic.CreateView, LoginRequiredMixin):
    model = Factory
    form_class = FactoryForm
    template_name = 'factory-create.html'
    success_url = reverse_lazy('factory:factory-view')


class FactoryListView(generic.ListView, LoginRequiredMixin):
    model = Factory
    template_name ='factory-view.html'
    paginate_by = 50
    ordering = ['factory_code']


class FactoryUpdate(generic.UpdateView, LoginRequiredMixin):
    model = Factory
    template_name = 'factory-update.html'
    form_class = FactoryForm
    success_message = "Updated successfully!"
    success_url = reverse_lazy('factory:factory-view')


class FactoryDelete(generic.DeleteView, LoginRequiredMixin):
    model = Factory
    template_name = 'factory-delete.html'
    success_message = 'Deleted Successfully!'
    success_url = reverse_lazy('factory:factory-view')
