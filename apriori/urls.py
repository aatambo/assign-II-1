from django.urls import path

from .views import CsvCreateView, CsvDetailView, CsvListView

urlpatterns = [
    path("", CsvListView.as_view(), name="csv-list"),
    path("add/", CsvCreateView.as_view(), name="csv-add"),
    path("<int:pk>/", CsvDetailView.as_view(), name="csv-detail"),
]
