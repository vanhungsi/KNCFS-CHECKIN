# from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from .models import Checkin
from django.views import generic
from .forms import CheckinForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages

# Create your views here.


class CheckinCreateView(generic.CreateView, SuccessMessageMixin):
    model = Checkin
    form_class = CheckinForm
    template_name = 'checkin-create.html'
    success_url = reverse_lazy('checkin:checkin-create')
    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Thông tin check-in của bạn đã được gửi thành công.")  
        return super().form_valid(form)




class CheckinListView(generic.ListView, LoginRequiredMixin, ):
    model = Checkin
    template_name ='checkin-view.html'
    ordering = ['-checkin_time']

    def get_queryset(self):
        queryset = super().get_queryset()
        selected_date = self.request.GET.get('date', None)
        if selected_date:
            try:
                date_object = datetime.strptime(selected_date, '%Y-%m-%d').date()
            except ValueError:
                date_object = timezone.now().date()
        else:
            date_object = timezone.now().date()
        return queryset.filter(checkin_time__date=date_object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context


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