from django.urls import path
from .views import *

# Create your tests here.
urlpatterns= [
    path('dashboard_view/',dashboard_view,name='dashboard_view'),
    path('',login_view,name='login_view'),
    path('register_view/',register_view,name='register_view'),
    path('forgot_password_view/',forgot_password_view,name='forgot_password_view'),
    path('otp_verification_view/',otp_verification_view,name='otp_verification_view'),
    path('patient_dashboard_view/',patient_dashboard_view,name='patient_dashboard_view'),
    path('logout/',logout,name='logout'),
    path('profile_view/',profile_view,name='profile_view'),
    path('appointment_form_view/',appointment_form_view,name='appointment_form_view'),
    path('update_patient_view/<int:id>',update_patient_view,name='update_patient_view'),
    path('delete_patient_view/<int:id>',delete_patient_view,name='delete_patient_view'),
]