from django.urls import path
from checkin import views
from django.contrib.auth.decorators import login_required

app_name = 'checkin'

urlpatterns = [
    path("create/", views.CheckinCreateView.as_view(), name="checkin-create"),
    path("view/", login_required(views.CheckinListView.as_view(), login_url='users:login'), name="checkin-view"),
    path("update/<int:pk>/", login_required(views.CheckinUpdate.as_view(),login_url='users:login'), name="checkin-update"),
    path("delete/<int:pk>/", login_required(views.CheckinDelete.as_view(),login_url='users:login'), name='checkin-delete'),
]