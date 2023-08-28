from django.urls import path,include
from PHR import  views
urlpatterns=[
    path('basic_input/',views.basic_input),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", views.dashboard, name="dashboard"),


    path("document_category/", views.document_category, name="document_category"),
    path("purpose_master/", views.purpose_master, name="purpose_master"),
    path("hospital_master/", views.hospital_master, name="hospital_master"),
    
    path("patient_profile/", views.patient_profile, name="patient_profile"),
    path("my_profile/", views.my_profile, name="my_profile"),
    path("medical_history/", views.medical_history, name="medical_history"),
    path("prescriptions/", views.prescriptions, name="prescriptions"),
    path("view_prescription/", views.view_prescription, name="view_prescription"),
    path("delete_document/<pk>", views.delete_document, name="delete_document"),
]