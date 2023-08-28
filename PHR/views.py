from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from PHR.models import *
from PHR.forms import *
from datetime import date
from datetime import *
from datetime import datetime


# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/login_request")
		else:
			messages.warning(request, form.errors )
			print(form.errors)
	form = NewUserForm()
	return render (request,"register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			if request.user.is_superuser:
				return redirect('/login_request')
			else:
				return redirect('/dashboard')
		else:
			messages.warning(request, 'Username or password is worng.')
	return render(request, 'login.html')

def basic_input(request):
    return render(request,'forms-basic-inputs.html')

def dashboard(request):
    context={
	    'dashboard':'active'
	}
    return render(request,'dashboard.html',context)

def document_category(request):
    records=DocumentCategoryMaster.objects.all()
    doc_cate_form =DocumentCategoryMasterForm()
    if request.method=='POST':
        doc_cate_form=DocumentCategoryMasterForm(request.POST)
        if doc_cate_form.is_valid():
            doc_cate_form.save()
            return redirect('/document_category')
    context={
	    'doc_category_active':'active','doc_category_open':'open','records':records,'doc_cate_form':doc_cate_form
	}
    return render(request,'master/document_category.html',context)

def purpose_master(request):
    records=PurposeMaster.objects.all()
    purpose_form =PurposeMasterForm()
    if request.method=='POST':
        purpose_form=PurposeMasterForm(request.POST)
        if purpose_form.is_valid():
            purpose_form.save()
            return redirect('/purpose_master')
    context={
	    'purpose_active':'active','purpose_open':'open','records':records,'purpose_form':purpose_form
	}
    return render(request,'master/purpose_master.html',context)

def hospital_master(request):
    records=HospitalMaster.objects.all()
    hospi_form =HospitalMasterForm()
    if request.method=='POST':
        hospi_form=HospitalMasterForm(request.POST)
        if hospi_form.is_valid():
            hospi_form.save()
            return redirect('/hospital_master')
    context={
	    'hospital_active':'active','hospital_open':'open','records':records,'hospi_form':hospi_form
	}
    return render(request,'master/hospital_master.html',context)

def patient_profile(request):
	if request.method == 'POST':
		patient_profile = Patient_Profile(
			user_id_id = request.user,
			title = request.POST.get('title'),
			first_name = request.POST.get('first_name'),
			middle_name = request.POST.get('middle_name'),
			last_name = request.POST.get('last_name'),
			age = request.POST.get('age'),
			dob = request.POST.get('dob'),
			gender = request.POST.get('gender'),
			blood_group = request.POST.get('blood_group'),
			marital_status = request.POST.get('marital_status'),
			father_name = request.POST.get('father_name'),
			mobile_number = request.POST.get('mobile_number'),
			email_id = request.POST.get('email_id'),
			address = request.POST.get('address'),
			country = request.POST.get('country'),
			state = request.POST.get('state'),
			city = request.POST.get('city'),
			pin_code = request.POST.get('pin_code'),
			profile_photo = request.POST.get('profile_photo'),
			
		)
		patient_profile.save()
		return redirect('/patient_profile')
	context={
		'patient_profile_active':'active','patient_profile_open':'open'
	}
	return render(request,'profile/patient_profile.html',context)

def my_profile(request):
	user_detail = Patient_Profile.objects.filter(user_id_id=request.user).first()
	if request.method == 'POST':
		user_detail.first_name=request.POST.get('firstName')
		user_detail.last_name=request.POST.get('lastName')
		user_detail.email_id=request.POST.get('email')
		user_detail.mobile_number=request.POST.get('phoneNumber')
		user_detail.address=request.POST.get('address')
		user_detail.state=request.POST.get('state')
		user_detail.pin_code=request.POST.get('zipCode')
		user_detail.country=request.POST.get('country')
		user_detail.save()

		return redirect('/my_profile')
	context={
		'user_detail':user_detail
	}
	return render(request,'profile/my_profile.html',context)

def medical_history(request):
	if request.method == 'POST':
		prescriptions=request.FILES.get('prescriptions')
		# history=History(
		# 	prescription=prescriptions
		# )
		# history.save()
	context={
		'mh_active':'active','mh_open':'open'
	}
	return render(request,'medical_history/medical_history.html',context)

def prescriptions(request):
    purpose = PurposeMaster.objects.all()
    doc_type = DocumentCategoryMaster.objects.all()
    hospital = HospitalMaster.objects.all()

    if request.method == 'POST':
        pre_id = Prescription_Detail.objects.count()
        today = datetime.today().strftime("%d%m%y")
        prescrip_no = f'PN{today}000{pre_id}'
        document = request.FILES.get('document')

        prescrip_detail = Prescription_Detail(
            prescrip_no=prescrip_no,
            date=datetime.now(),
            doc_type_id=request.POST.get('doc_type'),
            purpose_id=request.POST.get('purpose'),
            document=document,
            hospital_id=request.POST.get('hospital_name'),
            doctor=request.POST.get('doctor_name'),
            user_id_id=request.user.id,
        )
        prescrip_detail.save()
        return redirect('/prescriptions')

    context = {
        'pre_active': 'active',
        'pre_open': 'open',
        'purpose': purpose,
        'doc_type': doc_type,
        'hospital': hospital,
    }
    return render(request, 'prescriptions/prescriptions.html', context)

def view_prescription(request):
	prescrip_detail = Prescription_Detail.objects.filter(user_id_id=request.user)
	delete_temp = request.POST.get('delete_temp')
	if delete_temp == 'delete_temp':
		temp_id = request.POST.get('temp_id')
		prescrip_delete = Prescription_Detail.objects.filter(id=temp_id).delete()
		return redirect('/view_prescription')
	context={
		'pre_active':'active','pre_open':'open','prescrip_detail':prescrip_detail
	}
	return render(request,'prescriptions/view_prescription.html',context)

def delete_document(request,pk):
	prescrip_delete = Prescription_Detail.objects.filter(id=pk).delete()
	return HttpResponseRedirect('/view_prescription')
