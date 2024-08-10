from django.urls import path
from checkin import views

app_name = 'checkin'

urlpatterns = [
    path("create/", views.CheckinCreateView.as_view(), name="checkin-create"),

]