from django.urls import path
from factory import views

app_name = 'factory'

urlpatterns = [
    path("create/", views.FactoryCreateView.as_view(), name="factory-create"),
    path("view/", views.FactoryListView.as_view(), name="factory-view"),
    path("update/<int:pk>/", views.FactoryUpdate.as_view(), name="factory-update"),
    path("delete/<int:pk>/", views.FactoryDelete.as_view(), name='factory-delete'),
]