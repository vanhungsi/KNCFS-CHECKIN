from django.contrib import messages
from django.contrib.auth import logout as user_logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import FormView


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'users\login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('checkin:checkin-view')


def logout(request):
    user_logout(request)
    messages.info(request, "Logged out successfully")
    return HttpResponseRedirect(reverse("users:login"))

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('checkin:checkin-view')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

