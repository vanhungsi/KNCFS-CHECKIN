from django.urls import path
from factory import views
from django.contrib.auth.decorators import login_required

app_name = 'factory'

urlpatterns = [
    path("create/", login_required(views.FactoryCreateView.as_view(), login_url='users:login'), name="factory-create"),
    path("view/", login_required(views.FactoryListView.as_view(), login_url='users:login'), name="factory-view"),
    path("update/<int:pk>/", login_required(views.FactoryUpdate.as_view(), login_url='users:login'), name="factory-update"),
    path("delete/<int:pk>/", login_required(views.FactoryDelete.as_view(), login_url='users:login'),name='factory-delete'),
]