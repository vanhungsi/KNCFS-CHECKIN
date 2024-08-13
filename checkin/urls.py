from django.urls import path
from checkin import views

app_name = 'checkin'

urlpatterns = [
    path("create/", views.CheckinCreateView.as_view(), name="checkin-create"),
    path("view/", views.CheckinListView.as_view(), name="checkin-view"),
    path("update/<int:pk>/", views.CheckinUpdate.as_view(), name="checkin-update"),
    path("delete/<int:pk>/", views.CheckinDelete.as_view(), name='checkin-delete'),
]