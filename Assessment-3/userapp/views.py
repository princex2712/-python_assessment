from django.shortcuts import render,redirect
from authentication.models import UserModel,AppointmentModel
from django.contrib import messages

from PIL import Image
from io import BytesIO

from master.utils.HF_GENERATE.generate_otp import generate_otp


def dashboard_view(request):
    """
    Renders the dashboard view.

    Retrieves a list of doctors and appointments for the current user.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Renders the dashboard template with context data.
    """
    doctors = UserModel.objects.filter(role='doctor').exclude(id=request.session['id'])
    getappointments = AppointmentModel.objects.filter(doctor_id=request.session['id'])
    context = {
        'patients':getappointments,
        'doctors':doctors
    }
    return render(request,'userapp/dashboard.html',context)

def login_view(request):
    """
    Handles user login.

    Authenticates user credentials and sets session variables upon successful login.
    Redirects to the appropriate dashboard based on the user's role.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Renders the login template or redirects to the dashboard.
    """
    if request.method == "POST":
        email_ = request.POST['email']
        password_ = request.POST['password'] 
        role_ = request.POST['role']
        try:
            getUser = UserModel.objects.get(email = email_)
        except UserModel.DoesNotExist:
            messages.warning(request,"User Does Not Exist!")
            return render(request,'userapp/login.html')
        else:
            if getUser:
                if getUser.password == password_:
                    if getUser.role == role_:
                        request.session['id'] = getUser.id
                        request.session['first_name'] = getUser.first_name
                        request.session['last_name'] = getUser.last_name
                        request.session['email'] = getUser.email
                        request.session['contact'] = getUser.contact
                        request.session['role'] = getUser.role
                        if role_ == "patient":
                            messages.success(request,"Login Success!")
                            return redirect('patient_dashboard_view')
                        elif role_ == "doctor":
                            messages.success(request,"Login Success!")
                            return redirect('dashboard_view')
                    else:
                        messages.warning(request,"Invalid User Role Or Not Registered")
                        return render(request,'userapp/login.html')
                else:
                    messages.warning(request,"Invalid User Password!")
                    return render(request,'userapp/login.html')
            else:
                messages.warning(request,"User Does Not Exist!")
                return render(request,'userapp/login.html')
    if 'email' in request.session:\
        return render(request,'userapp/dashboard.html')

    return render(request,'userapp/login.html')

def register_view(request):
    """
    Renders the registration view.

    Handles user registration form submission and creates a new user.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Renders the registration template.
    """
    
    if request.method == "POST":
        try:
            first_name_ = request.POST['first_name']
            last_name_ = request.POST['last_name']
            email_ = request.POST['email']
            contact_ = request.POST['contact']
            role_ = request.POST['role']

            if UserModel.objects.filter(email=email_).exists():
                messages.warning(request,"Email Already taken!")
                return redirect('register_view')
        except Exception as e:
            print(e)
        else:
            new_user = UserModel(first_name=first_name_, last_name=last_name_, email=email_, contact=contact_, role=role_)
            new_user.save()
            messages.success(request,"Registered Successfully!")
            return redirect('login_view')
    return render(request,'userapp/register.html')

def forgot_password_view(request):
    """
    Renders the forgot password view.

    Handles the submission of the forgot password form, generates and verifies OTP,
    and allows users to reset their passwords.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Renders the forgot password template.
    """
    if request.method == "POST":
        role_ = request.POST['role']
        email_ = request.POST['email']
        try:
            getUser = UserModel.objects.get(email=email_)
        except UserModel.DoesNotExist:
            messages.warning(request,'User Does Not Exist')
            return render(request,'userapp/forgot_password.html')
        else: 
            if getUser:
                if role_ == getUser.role:
                    otp_ = generate_otp()
                    getUser.otp = otp_
                    getUser.save()
                    messages.success(request,f"OTP sent to {email_} Successfully!")
                    context = {
                        'email':email_
                    }
                    return render(request,'userapp/otp_verification.html',context)
                else:
                    messages.warning(request,'Invalid Email or Role!')
                    return render(request,'userapp/forgot_password.html')
            else:
                messages.warning(request,'User Does Not Exist')
                return render(request,'userapp/forgot_password.html')
    return render(request,'userapp/forgot_password.html')

def otp_verification_view(request):
    """
    Renders the OTP verification view.

    Handles OTP submission and verifies it to reset the user's password.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Renders the OTP verification template.
    """
    if request.method == "POST":
        email_ = request.POST['email']
        otp_ = request.POST['otp']
        password_ = request.POST['password']
        confirm_password = request.POST['c_password']
        try:
            getUser = UserModel.objects.get(email=email_)
        except UserModel.DoesNotExist:
            messages.warning(request,'User Does Not Exist')
            return render(request,'userapp/forgot_password.html')
        else:
            if getUser:
                if otp_ == getUser.otp:
                    if password_ == confirm_password:
                        getUser.password = password_
                        getUser.save()
                        messages.success(request,"Password Reset Successfully")
                        return redirect('login_view')
                    else:
                        messages.warning(request,"Password Does Not Match!")
                        context = {
                            'email':email_
                        }
                        return render(request,'userapp/otp_verification.html',context)
                else:
                    messages.warning(request,"Wrong OTP!")
                    otp_ = generate_otp()
                    getUser.otp = otp_
                    getUser.save()
                    context = {
                            'email':email_
                        }
                    return render(request,'userapp/otp_verification.html',context)
            else:
                messages.warning(request,'User Does Not Exist')
                return render(request,'userapp/forgot_password.html')
    return render(request,'userapp/otp_verification.html')

def patient_dashboard_view(request):
    """
    Renders the patient dashboard view.

    Retrieves a list of doctors for patient appointments.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Renders the patient dashboard template with context data.
    """
    doctors = UserModel.objects.filter(role='doctor')
    context = {
        'doctors':doctors
    }
    return render(request,'userapp/patient_dashboard.html',context)

def logout(request):
    """
    Logs out the user.

    Clears session data and redirects to the login view.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponseRedirect: Redirects to the login view.
    """
    request.session.clear()
    return redirect('login_view') 

def profile_view(request):
    """
    Renders the user profile view.

    Retrieves and displays user profile information.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Renders the user profile template with context data.
    """
    context = {
        'first_name':request.session['first_name'],
        'last_name':request.session['last_name'],
        'email':request.session['email'],
        'contact':request.session['contact'],
    }
    return render(request,'userapp/profile.html',context)

def appointment_form_view(request):
    """
    Renders the appointment form view.

    Renders the appointment form and handles form submission for appointment registration.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Renders the appointment form template.
    """
    if request.method=="GET":
        is_new_appointment = AppointmentModel.objects.filter(patient_id_id=request.session['id'])
        if is_new_appointment:
            messages.warning(request,"You can Register only 1 Appointment at a Time!")
            return redirect('profile_view')
        doctor_id_ = request.GET.get('doctor_id')
        doctor = UserModel.objects.get(id=doctor_id_) 
        patient = UserModel.objects.get(id=request.session['id'])
        context = {
            'doctor_first_name': doctor.first_name,
            'doctor_last_name': doctor.last_name,
            'select_doctor_id':doctor.id,
            'patient':patient
        }
        return render(request, 'userapp/appointment_form.html', context)
    if request.method=="POST":
        try:
            first_name_ = request.POST['first_name']
            last_name_ = request.POST['last_name']
            contact_ = request.POST['contact']
            age_ = request.POST['age']
            address_ = request.POST['address']
            gender_ = request.POST['gender']
            doctor_id_ = request.POST['select_doctor_id']
            patient_id_id_ = request.session['id']
            
        except Exception as e:
            messages.error(request, f'ERROR: {str(e)}')
            return render(request,'userapp/appointment_form.html')
        else:
            appointment = AppointmentModel(doctor_id=doctor_id_,patient_id_id=patient_id_id_, first_name=first_name_, last_name=last_name_, contact=contact_, age=age_, address=address_, gender= gender_)
            appointment.save()
            messages.success(request, f'Appointment for {first_name_} {last_name_} is added.')
            return redirect('patient_dashboard_view')

def update_patient_view(request,id):
    """
    Renders the update patient view.

    Renders the update patient form and handles form submission for updating patient information.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - id (int): The ID of the patient to be updated.

    Returns:
    - HttpResponse: Renders the update patient template with context data.
    """
    getpatient = AppointmentModel.objects.get(id=id)
    if request.method=="POST":
        try:
            first_name_ = request.POST['first_name']
            last_name_ = request.POST['last_name']
            contact_ = request.POST['contact']
            age_ = request.POST['age']
            gender_ = request.POST['gender']
            address_ = request.POST['address']
            notes_ = request.POST['notes']
            status_ = request.POST['status']
        except Exception as e:
            messages.error(request,f"Error: {str(e)}")
            return redirect('dashboars_view')
        else:
            getpatient.first_name = first_name_
            getpatient.last_name = last_name_
            getpatient.contact = contact_
            getpatient.age = age_
            getpatient.gender = gender_
            getpatient.address = address_
            getpatient.status = status_
            getpatient.notes = notes_
            getpatient.save()
            messages.success(request,f"{first_name_} {last_name_} Update Successfully!")
            return redirect('dashboard_view')

    context = {
        'first_name':getpatient.first_name,
        'last_name':getpatient.last_name,
        'contact':getpatient.contact,
        'gender':getpatient.gender,
        'address':getpatient.address,
        'age':getpatient.age,
        'notes':getpatient.notes,
        'status':getpatient.status
    }
    return render(request,'userapp/update_patient.html',context)

def delete_patient_view(request,id):
    """
    Deletes a patient record.

    Deletes the specified patient record and redirects to the dashboard view.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - id (int): The ID of the patient to be deleted.

    Returns:
    - HttpResponseRedirect: Redirects to the dashboard view.
    """
    getpatient = AppointmentModel.objects.get(id=id)
    messages.success(request,f"{getpatient.first_name} {getpatient.last_name} is Deleted Successfully!")
    getpatient.delete()
    return redirect('dashboard_view')

def doctor_profile_view(request):
    """
    Renders the doctor profile view.

    Renders the doctor profile form and handles form submission for doctor profile creation.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Renders the doctor profile template.
    """
    if request.method == "POST":
        try:
            first_name_ = request.POST['first_name']
            last_name_ = request.POST['last_name']
            email_ = request.POST['email']
            contact_ = request.POST['contact']
            role_ = request.POST['role']
            speciality_ = request.POST['speciality']
            photo_ = request.FILES['image']
            if UserModel.objects.filter(email=email_).exists():
                messages.warning(request,"Email Already taken!")
                return redirect('doctor_profile_view')
        except Exception as e:
            print(e)
        else:
            image = Image.open(photo_)
            image.thumbnail((300, 300))

            image_io = BytesIO()
            image.save(image_io, format='PNG')
            image_io.seek(0)
            
            new_user = UserModel(first_name=first_name_, last_name=last_name_, email=email_, contact=contact_, role=role_, doctor_speciality=speciality_,photo = photo_ )
            new_user.save()
            messages.success(request,"Registered Successfully!")
            return redirect('login_view')
    return render(request,'userapp/doctor_profile.html')

def appointment_status_view(request):
    """
    Renders the appointment status view.

    Retrieves the appointment details and associated doctor for the logged-in patient.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Renders the appointment status template with context data.
    """
    try:
        appointment = AppointmentModel.objects.get(patient_id_id=request.session['id'])
        doctor = UserModel.objects.get(id=appointment.doctor_id)
        context = {
            'appointment': appointment,
            'doctor': doctor
        }
        return render(request, 'userapp/appointment_status.html', context)
    except AppointmentModel.DoesNotExist:
        messages.info(request, 'No appointments registered.')
        return redirect('patient_dashboard_view')
    except UserModel.DoesNotExist:
        messages.info(request, 'Doctor is not available')
        return redirect('patient_dashboard_view')