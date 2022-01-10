from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from . import forms
from . import models
def patientcall(request,book_id):
    book_id = int(book_id)
    obj=models.makeappointments.objects.get(id=book_id)
    patient_id=obj.patientid_id
    doctor_id=obj.doctorid_id
    object=models.patientlogin.objects.get(id=patient_id)
    object2=models.doctorlogin.objects.get(id=doctor_id)
    return render(request, 'index1.html',{'id2':object,'id':object2})

def doctormakecall(request,book_id):
    book_id = int(book_id)
    obj=models.makeappointments.objects.get(id=book_id)
    patient_id=obj.patientid_id
    doctor_id=obj.doctorid_id
    object=models.patientlogin.objects.get(id=patient_id)
    object2=models.doctorlogin.objects.get(id=doctor_id)
    return render(request, 'index1.html',{'id':object,'id2':object2})
# Create your views here.
def index(request):
    return render(request, 'index1.html')
def appointmenthasmade(request):    
    if request.method=='POST':
        date=request.POST['date']
        select=request.POST['select']
        doctorid=request.POST['id']
        time=request.POST['time']
        patient_id=request.session.get('patient_id')
        patients=models.patientlogin.objects.get(id=patient_id)
        doctors=models.doctorlogin.objects.get(id=doctorid)
        status="confirmed"
        object=models.makeappointments(date=date, paymentmethod=select,doctorid=doctors,patientid=patients,appoointmentstatus=status, time=time)
        object.save()
        base_url ="/call"
        Chosen_url="/Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)

def makeappointment(request,book_id):
    book_id = int(book_id)
    return render(request, 'Make-Appointments.html',{"id":book_id})    

    
def changedoctorpicture(request):
    if request.method == 'POST' :
        patient_id=request.session.get('doctor_id')
        patients=models.doctorlogin.objects.get(id=patient_id)
       #patient_id=request.session.get('patient_id')
       
        upload= forms.doctorprofile(data=request.POST or None, files=request.FILES, instance=patients)
        if upload.is_valid():
            upload.save()
        base_url ="/call"
        Chosen_url="/Doctor-Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)

def changepatientpicture(request):
    if request.method == 'POST' :
        patient_id=request.session.get('patient_id')
        patients=models.patientlogin.objects.get(id=patient_id)
       #patient_id=request.session.get('patient_id')
       
        upload= forms.patientprofile(data=request.POST or None, files=request.FILES, instance=patients)
        if upload.is_valid():
            upload.save()
        base_url ="/call"
        Chosen_url="/Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)

def changedoctorpassword(request):
    if request.method == 'POST':
        patient_id=request.session.get('doctor_id')
        patients=models.doctorlogin.objects.get(id=patient_id)
        
       #patient_id=request.session.get('patient_id')
        oldpasword=request.POST['oldpasword']
        newpassword=request.POST['newpassword']
        confirmPassword=request.POST['confirmPassword']
        if newpassword!=confirmPassword:return render(request, 'Doctor-Profile-Set.html',{'pat':patients,"error":"confirm password and new password are not smae"})
        if oldpasword!=patients.password:return render(request, 'Doctor-Profile-Set.html',{'pat':patients,"error":"Old password is not correct"})
        patients.password=newpassword
        patients.save()
        base_url ="/call"
        Chosen_url="/Doctor-Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)


def changepatientpassword(request):
    if request.method == 'POST':
        patient_id=request.session.get('patient_id')
        patients=models.patientlogin.objects.get(id=patient_id)
        
       #patient_id=request.session.get('patient_id')
        oldpasword=request.POST['oldpasword']
        newpassword=request.POST['newpassword']
        confirmPassword=request.POST['confirmPassword']
        if newpassword!=confirmPassword:return render(request, 'Patient-Profile-Set.html',{'pat':patients,"error":"confirm password and new password are not smae"})
        if oldpasword!=patients.password:return render(request, 'Patient-Profile-Set.html',{'pat':patients,"error":"Old password is not correct"})
        patients.password=newpassword
        patients.save()
        base_url ="/call"
        Chosen_url="/Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)

def changedoctorprofile(request):
    if request.method == 'POST':
        patient_id=request.session.get('doctor_id')
        patients=models.doctorlogin.objects.get(id=patient_id)
        
       #patient_id=request.session.get('patient_id')
        name=request.POST['name']
        email=request.POST['email']
        DOB=request.POST['DOB']
        phone=request.POST['phone']
        City=request.POST['City']
        cnic=request.POST['cnic']
        patients.name=name
        patients.email=email
        patients.DOB=DOB
        patients.phone=phone
        patients.City=City
        patients.cnic=cnic
        patients.save()
        base_url ="/call"
        Chosen_url="/Doctor-Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)


def changepatientprofile(request):
    if request.method == 'POST':
        patient_id=request.session.get('patient_id')
        patients=models.patientlogin.objects.get(id=patient_id)
        
       #patient_id=request.session.get('patient_id')
        name=request.POST['name']
        email=request.POST['email']
        DOB=request.POST['DOB']
        phone=request.POST['phone']
        City=request.POST['City']
        cnic=request.POST['cnic']
        patients.name=name
        patients.email=email
        patients.DOB=DOB
        patients.phone=phone
        patients.City=City
        patients.cnic=cnic
        patients.save()
        base_url ="/call"
        Chosen_url="/Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)

def doctoraddeditjazzcash(request):
    if request.method == 'POST':
        name=request.POST['name']
        phone=request.POST['phone']
        patient_id=request.session.get('doctor_id')
        patients=models.doctorlogin.objects.get(id=patient_id)
        try:
            credit_form=models.doctorjazzcash.objects.get(doctorid_id=patient_id)
        except models.doctorjazzcash.DoesNotExist :
            
            object=models.doctorjazzcash(name=name,phone=phone,doctorid=patients)
            object.save()
            base_url ="/call"
            Chosen_url="/Doctor-Profile-Settings"
            url = "{}{}".format(base_url, Chosen_url)
            return redirect(url)
        credit_form.name=name
        credit_form.phone=phone

        #return render(request, 'test.html',{'pat':expirydate})
        credit_form.save()
        base_url ="/call"
        Chosen_url="/Doctor-Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)


def addeditjazzcash(request):
    if request.method == 'POST':
        name=request.POST['name']
        phone=request.POST['phone']
        patient_id=request.session.get('patient_id')
        patients=models.patientlogin.objects.get(id=patient_id)
        try:
            credit_form=models.jazzcash.objects.get(patientid_id=patient_id)
        except models.jazzcash.DoesNotExist :
            
            object=models.jazzcash(name=name,phone=phone,patientid=patients)
            object.save()
            base_url ="/call"
            Chosen_url="/Profile-Settings"
            url = "{}{}".format(base_url, Chosen_url)
            return redirect(url)
        credit_form.name=name
        credit_form.phone=phone

        #return render(request, 'test.html',{'pat':expirydate})
        credit_form.save()
        base_url ="/call"
        Chosen_url="/Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)

def doctoraddediteasypaisa(request):
    if request.method == 'POST':
        name=request.POST['name']
        phone=request.POST['phone']
        patient_id=request.session.get('doctor_id')
        patients=models.doctorlogin.objects.get(id=patient_id)
        try:
            credit_form=models.doctoreasypaisa.objects.get(doctorid_id=patient_id)
        except models.doctoreasypaisa.DoesNotExist :
            
            object=models.doctoreasypaisa(name=name,phone=phone,doctorid=patients)
            object.save()
            base_url ="/call"
            Chosen_url="/Doctor-Profile-Settings"
            url = "{}{}".format(base_url, Chosen_url)
            return redirect(url)
        credit_form.name=name
        credit_form.phone=phone

        #return render(request, 'test.html',{'pat':expirydate})
        credit_form.save()
        base_url ="/call"
        Chosen_url="/Doctor-Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)

def addediteasypaisa(request):
    if request.method == 'POST':
        name=request.POST['name']
        phone=request.POST['phone']
        patient_id=request.session.get('patient_id')
        patients=models.patientlogin.objects.get(id=patient_id)
        try:
            credit_form=models.easypaisa.objects.get(patientid_id=patient_id)
        except models.easypaisa.DoesNotExist :
            
            object=models.easypaisa(name=name,phone=phone,patientid=patients)
            object.save()
            base_url ="/call"
            Chosen_url="/Profile-Settings"
            url = "{}{}".format(base_url, Chosen_url)
            return redirect(url)
        credit_form.name=name
        credit_form.phone=phone

        #return render(request, 'test.html',{'pat':expirydate})
        credit_form.save()
        base_url ="/call"
        Chosen_url="/Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)
            
        

def doctoraddeditcreditcard(request):
    if request.method == 'POST':
        name=request.POST['name']
        cardBran=request.POST['cardBrand']
        cardNumber=request.POST['cardNumber']
        CVV=request.POST['CVV']
        expirydate=request.POST['expirydate']

        patient_id=request.session.get('doctor_id')
        patients=models.doctorlogin.objects.get(id=patient_id)
        try:
            credit_form=models.doctorcreditcard.objects.get(doctorid_id=patient_id)
        except models.doctorcreditcard.DoesNotExist :
            
            object=models.doctorcreditcard(name=name,cardbrand=cardBran,cardno=cardNumber,CVV=CVV,expirydate=expirydate,doctorid=patients)
            object.save()
            base_url ="/call"
            Chosen_url="/Doctor-Profile-Settings"
            url = "{}{}".format(base_url, Chosen_url)
            return redirect(url)
        credit_form.name=name
        credit_form.cardbrand=cardBran
        credit_form.cardno=cardNumber
        credit_form.CVV=CVV
        #return render(request, 'test.html',{'pat':expirydate})
        credit_form.expirydate=expirydate
        credit_form.save()
        base_url ="/call"
        Chosen_url="/Doctor-Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)

def addeditcreditcard(request):
    if request.method == 'POST':
        name=request.POST['name']
        cardBran=request.POST['cardBrand']
        cardNumber=request.POST['cardNumber']
        CVV=request.POST['CVV']
        expirydate=request.POST['expirydate']

        patient_id=request.session.get('patient_id')
        patients=models.patientlogin.objects.get(id=patient_id)
        try:
            credit_form=models.creditcard.objects.get(patientid_id=patient_id)
        except models.creditcard.DoesNotExist :
            
            object=models.creditcard(name=name,cardbrand=cardBran,cardno=cardNumber,CVV=CVV,expirydate=expirydate,patientid=patients)
            object.save()
            base_url ="/call"
            Chosen_url="/Profile-Settings"
            url = "{}{}".format(base_url, Chosen_url)
            return redirect(url)
        credit_form.name=name
        credit_form.cardbrand=cardBran
        credit_form.cardno=cardNumber
        credit_form.CVV=CVV
        #return render(request, 'test.html',{'pat':expirydate})
        credit_form.expirydate=expirydate
        credit_form.save()
        base_url ="/call"
        Chosen_url="/Profile-Settings"
        url = "{}{}".format(base_url, Chosen_url)
        return redirect(url)
            

def deleteDoctor_session(request):
    try:
        del request.session['doctor_id']
        del request.session['doctor']
    except  KeyError:
        pass
    base_url ="/call"
    Chosen_url=""
    url = "{}{}".format(base_url, Chosen_url)
    return redirect(url)    

def deletePatient_session(request):
    try:
        del request.session['patient_id']
        del request.session['patient']
    except  KeyError:
        pass
    base_url ="/call"
    Chosen_url=""
    url = "{}{}".format(base_url, Chosen_url)
    return redirect(url)    
def DoctorProfileSettings(request):
    if request.session.get('doctor'):
        doctor_id=request.session.get('doctor_id')
        patients=models.doctorlogin.objects.get(id=doctor_id)
        upload=forms.doctorprofile()
        credit=True
        easypaisa=True
        jazzcash=True
        appointments=True
        try:
            credit_form=models.doctorcreditcard.objects.get(doctorid_id=doctor_id)
        except models.doctorcreditcard.DoesNotExist :
            credit=False
        try:
            easypaisa_form=models.doctoreasypaisa.objects.get(doctorid_id=doctor_id)
        except models.doctoreasypaisa.DoesNotExist :
            easypaisa=False
        try:
            jazz_form=models.doctorjazzcash.objects.get(doctorid_id=doctor_id)
        except models.doctorjazzcash.DoesNotExist :
            jazzcash=False
        try:
            appointment_form=models.makeappointments.objects.all().filter(doctorid_id=doctor_id)
        except models.makeappointments.DoesNotExist:
            appointments=False
        if credit and easypaisa and jazzcash:
            return render(request, 'Doctor-Profile-Set.html',{'pat':patients,'upload_form':upload,"credit_form":credit_form,'easypaisa_form':easypaisa_form,'jazzcash_form':jazz_form,"appointment_form":appointment_form})
        elif credit and easypaisa:
            return render(request, 'Doctor-Profile-Set.html',{'pat':patients,'upload_form':upload,"credit_form":credit_form,'easypaisa_form':easypaisa_form,"appointment_form":appointment_form})
        elif easypaisa and jazzcash:
            return render(request, 'Doctor-Profile-Set.html',{'pat':patients,'upload_form':upload,'easypaisa_form':easypaisa_form,'jazzcash_form':jazz_form,"appointment_form":appointment_form})
        elif credit and jazzcash:
            return render(request, 'Doctor-Profile-Set.html',{'pat':patients,'upload_form':upload,"credit_form":credit_form,'jazzcash_form':jazz_form,"appointment_form":appointment_form})
        elif credit:
            return render(request, 'Doctor-Profile-Set.html',{'pat':patients,'upload_form':upload,"credit_form":credit_form,"appointment_form":appointment_form})
        elif jazzcash:
            return render(request, 'Doctor-Profile-Set.html',{'pat':patients,'upload_form':upload,'jazzcash_form':jazz_form,"appointment_form":appointment_form})
        elif easypaisa:
            return render(request, 'Doctor-Profile-Set.html',{'pat':patients,'upload_form':upload,'easypaisa_form':easypaisa_form,"appointment_form":appointment_form})
        else:
            return render(request, 'Doctor-Profile-Set.html',{'pat':patients,'upload_form':upload,"appointment_form":appointment_form})    


        
        
    else:
        return render(request, 'index.html',{'message':"You are not logged in as doctor"})    
def ProfileSettings(request):
    if request.session.get('patient'):
        patient_id=request.session.get('patient_id')
        patients=models.patientlogin.objects.get(id=patient_id)
        upload=forms.patientprofile()
        credit=True
        easypaisa=True
        jazzcash=True
        appointments=True
        try:
            credit_form=models.creditcard.objects.get(patientid_id=patient_id)
        except models.creditcard.DoesNotExist :
            credit=False
        try:
            easypaisa_form=models.easypaisa.objects.get(patientid_id=patient_id)
        except models.easypaisa.DoesNotExist :
            easypaisa=False
        try:
            jazz_form=models.jazzcash.objects.get(patientid_id=patient_id)
        except models.jazzcash.DoesNotExist :
            jazzcash=False
        try:
            appointment_form=models.makeappointments.objects.all().filter(patientid_id=patient_id)
        except models.makeappointments.DoesNotExist:
            appointments=False
        if credit and easypaisa and jazzcash:
            return render(request, 'Patient-Profile-Set.html',{'pat':patients,'upload_form':upload,"credit_form":credit_form,'easypaisa_form':easypaisa_form,'jazzcash_form':jazz_form,"appointment_form":appointment_form})
        elif credit and easypaisa:
            return render(request, 'Patient-Profile-Set.html',{'pat':patients,'upload_form':upload,"credit_form":credit_form,'easypaisa_form':easypaisa_form,'appointment_form':appointment_form})
        elif easypaisa and jazzcash:
            return render(request, 'Patient-Profile-Set.html',{'pat':patients,'upload_form':upload,'easypaisa_form':easypaisa_form,'jazzcash_form':jazz_form,'appointment_form':appointment_form})
        elif credit and jazzcash:
            return render(request, 'Patient-Profile-Set.html',{'pat':patients,'upload_form':upload,"credit_form":credit_form,'jazzcash_form':jazz_form,'appointment_form':appointment_form})
        elif credit:
            return render(request, 'Patient-Profile-Set.html',{'pat':patients,'upload_form':upload,"credit_form":credit_form,'appointment_form':appointment_form})
        elif jazzcash:
            return render(request, 'Patient-Profile-Set.html',{'pat':patients,'upload_form':upload,'jazzcash_form':jazz_form,'appointment_form':appointment_form})
        elif easypaisa:
            return render(request, 'Patient-Profile-Set.html',{'pat':patients,'upload_form':upload,'easypaisa_form':easypaisa_form,'appointment_form':appointment_form})
        else:
              return render(request, 'Patient-Profile-Set.html',{'pat':patients,'upload_form':upload,'appointment_form':appointment_form})


        
        
    else:
        return render(request, 'index.html',{'message':"You are not logged in as Patient"})
def homepage(request):
    shelf = models.doctorlogin.objects.all()
    return render(request, 'index.html',{'shelf': shelf})

def patientlogin(request):
    upload = forms.registrationalter()
    if request.method == 'POST':
        upload = forms.registrationalter(request.POST, request.FILES)
        email=request.POST['email']
        password=request.POST['password']
        if upload.is_valid():
            try:
                userexist=models.patientlogin.objects.get(Email=email,password=password)
            except models.patientlogin.DoesNotExist:
                return render(request, 'test.html', {'upload_form':"user not exists"}) 
            request.session['patient_id']=userexist.id
            request.session['patient']=True
            base_url ="/call"
            Chosen_url="/Profile-Settings"
            url = "{}{}".format(base_url, Chosen_url)
            return redirect(url)
            
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'Patient-Login.html', {'upload_form':upload})
    
    
def PatientRegistration(request):
    
    if request.method == 'POST' :
        upload = forms.patientloginform(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            base_url ="/call"
            Chosen_url=""
            url = "{}{}".format(base_url, Chosen_url)
            return redirect(url)
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        upload = forms.patientloginform()
        return render(request, 'Patient-Registration.html', {'upload_form':upload})
    
def RegistationDetails(request):
    return render(request, 'Registation-Details.html')
def DoctorLogin(request):
    
    upload = forms.doctorregistrationalter()
    if request.method == 'POST':
        upload = forms.doctorregistrationalter(request.POST, request.FILES)
        email=request.POST['email']
        password=request.POST['password']
        if upload.is_valid():
            try:
                userexist=models.doctorlogin.objects.get(Email=email,password=password)
            except models.doctorlogin.DoesNotExist:
                return render(request, 'test.html', {'upload_form':"user not exists"}) 
            request.session['doctor_id']=userexist.id
            request.session['doctor']=True
            base_url ="/call"
            Chosen_url="/Doctor-Profile-Settings"
            url = "{}{}".format(base_url, Chosen_url)
            return redirect(url)
            
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'Doctor-Login.html', {'upload_form':upload})

def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'test.html', {'file_url': file_url})
    return render(request, 'test.html')
       
def DoctorRegistration(request):
    upload = forms.doctorloginform()
    if request.method == 'POST':
        upload = forms.doctorloginform(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            base_url ="/call"
            Chosen_url=""
            url = "{}{}".format(base_url, Chosen_url)
            return redirect(url)
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'Doctor-Registration.html', {'upload_form':upload})
def DoctorRegistationDetails(request):
    return render(request, 'Doctor-Registation-Details.html')
def Appointment(request):
    patient_id=request.session.get('patient_id')
    patients=models.patientlogin.objects.get(id=patient_id)
    doctors=models.doctorlogin.objects.all()
    nearestdoctors=models.doctorlogin.objects.all()
    createdistanc=list()
    for object in nearestdoctors:
        createdistanc.append(creatdistance(object.id,haversine(patients.lattitude,patients.longitude,object.lattitude,object.longitude)))
    sorted_nearest= sorted(createdistanc, key= lambda e:e.distance)
    doctorslist=list()
    for obj in sorted_nearest:
        doctorslist.append(models.doctorlogin.objects.get(id=obj.id))
    return render(request, 'Appointment.html',{'shelf':doctors,'nearest':doctorslist})
def HelpPage(request):
    return render(request, 'Help-Page.html')



def index(request):
    shelf = models.patientlogin.objects.get(id='7')
    return render(request, 'test.html', {'shelf': shelf})


import math
def haversine(lat1, lon1, lat2, lon2):
     
    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
 
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) * math.cos(lat1) * math.cos(lat2))
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c
class creatdistance:
   
    def __init__(self, id,distance):
        self.id=id
        self.distance=distance
    