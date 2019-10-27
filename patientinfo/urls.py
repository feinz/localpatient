from django.urls import path
from . import views
from django.views.generic import TemplateView

#pattern for patientinfo application
urlpatterns = [
    path('', views.index, name='index'),
    path('patient_list/', views.PatientListView.as_view(), name='patient_list'),
    path('patient_detail/<int:pk>', views.PatientDetailView.as_view(), name='patient_detail'),
    path('patient/create/', views.PatientCreate.as_view(), name='patient_create'),
    path('patient_detail/<int:pk>/update/', views.PatientUpdate.as_view(), name='patient_detail_update'),
    path('patient_detail/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient_detail_delete'),

    # url to static html template
    # path('patient_deleted_success/', TemplateView.as_view(template_name="patient_deleted_success.html"), name='patient_deleted_success'),
]