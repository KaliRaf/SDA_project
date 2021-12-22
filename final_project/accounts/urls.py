from django.urls import path
from .views import PatientListView, PatientDetailView

urlpatterns = [
    path('patients', PatientListView.as_view(), name='patients'),
    path('patients/<int:pk>', PatientDetailView.as_view(), name='patient-detail'),
]
