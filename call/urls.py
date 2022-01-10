from django.urls import path

from . import views

urlpatterns = [
    path('videocall/', views.index, name='index'),
    path('', views.homepage, name='homepage'),
    path('Patient-Login/', views.patientlogin , name='patient'),
    path('Patient-Registration/', views.PatientRegistration , name='Patient-Registration'),
    path('Registation-Details/', views.RegistationDetails , name='Registation-Details'),
    path('Doctor-Login/', views.DoctorLogin , name='Doctor-Login'),
    path('Doctor-Registration/', views.DoctorRegistration , name='Doctor-Registration'),
    path('Doctor-Registation-Details/', views.DoctorRegistationDetails , name='Doctor-Registation-Details'),
    path('Appointment/', views.Appointment , name='Appointment'),
    path('Help-Page/', views.HelpPage , name='Help-Page'),
    path('Patient/', views.index , name='index'),
    path("upload/", views.upload, name="upload"),
    path("Profile-Settings/", views.ProfileSettings, name="Profile-Settings"),
    path("changepatientprofile/", views.changepatientprofile, name="changepatientprofile"),
    path("changepatientpassword/", views.changepatientpassword, name="changepatientpassword"),
    path("changepatientpicture/", views.changepatientpicture, name="changepatientpicture"),
    path("addeditcreditcard/", views.addeditcreditcard, name="addeditcreditcard"),
    path("addediteasypaisa/", views.addediteasypaisa, name="addediteasypaisa"),
    path("addeditjazzcash/", views.addeditjazzcash, name="addeditjazzcash"),
    path("Profile-Settings/deletePatient_session/", views.deletePatient_session, name="deletePatient_session"),
    path("Doctor-Profile-Settings/", views.DoctorProfileSettings, name="Profile-Settings"),
    
    path("changedoctorprofile/", views.changedoctorprofile, name="changedoctorprofile"),
    path("changedoctorpassword/", views.changedoctorpassword, name="changedoctorpassword"),
    path("changedoctorpicture/", views.changedoctorpicture, name="changedoctorpicture"),
    path("doctoraddeditcreditcard/", views.doctoraddeditcreditcard, name="doctoraddeditcreditcard"),
    path("doctoraddediteasypaisa/", views.doctoraddediteasypaisa, name="doctoraddediteasypaisa"),
    path("doctoraddeditjazzcash/", views.doctoraddeditjazzcash, name="doctoraddeditjazzcash"),
    path("Doctor-Profile-Settings/deleteDoctor_session/", views.deleteDoctor_session, name="deleteDoctor_session"),
    path("Appointment/makeappointment/<int:book_id>", views.makeappointment, name="makeappointment"),
    path("Appointment/appointmenthasmade/", views.appointmenthasmade, name="appointmenthasmade"),
   path("Doctor-Profile-Settings/doctormakecall/<int:book_id>", views.doctormakecall, name="doctormakecall"),
    path("Profile-Settings/patientcall/<int:book_id>", views.patientcall, name="patientcall"),
  
    
    



    
    
    

    






]