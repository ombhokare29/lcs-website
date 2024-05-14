from django.shortcuts import render, HttpResponse, redirect
from LCS.models import volunteer, sponsorship,Contact,create_checkout_session
from django.core.mail import send_mass_mail
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import stripe
from django.conf import settings

import random
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.
def index(request):
    # context = {
    #     "variable" : "made by om"
    # }
    # return HttpResponse("this is homepage")
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def joinus(request):
    return render(request, "joinus.html")
def donate(request):
    return render(request, "donate.html")
def checkout(request):
    return render(request, "checkout.html")

def volunteer_form(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        availability = request.POST.get('availability')
        print(name,email,phone,address,availability)
        ins = volunteer(name=name, email=email,phone=phone,address=address,availability=availability)
        ins.save()
        print("you response is save")
        
    return render(request, "volunteer.html")

def sponsorship_form(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        availability = request.POST.get('availability')
        print(name,email,phone,address,availability)
        ins = sponsorship(name=name, email=email,phone=phone,address=address,availability=availability)
        ins.save()
        print("you response is save")
        
    return render(request, "sponsorship.html")
    

def contact_form(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        print(name,email,phone,query)
        b = Contact(name=name,email=email,phone=phone,query=query)
        b.save()
        messages.success(request, "Your response hs been successfully sent!!")

    return render(request, 'contact.html')



@csrf_exempt
def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Generate a random 6-digit OTP
        otp = random.randint(10000000, 99999999)

        # Store the OTP in the session
        request.session['otp'] = otp
        request.session['otp_email'] = email

        # Send the OTP to the given email
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False
        )

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)



@csrf_exempt
def verify_otp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        otp = data.get('otp')

        # Check if OTP matches the one stored in the session
        if otp and str(request.session.get('otp')) == otp:
            return JsonResponse({'success': True})

        return JsonResponse({'success': False, 'error': 'Invalid OTP'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)


def handel_signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname= request.POST.get('lname')
        username= request.POST.get('username')
        email= request.POST.get('email')
        pass1= request.POST.get('pass1')
        pass2= request.POST.get('pass2')

        # basic checks
        if len(username)>15 or len(username)<4:
            messages.error(request, "Username should be grater than 3 letters and less than 15 letters. Try again")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and number. Try again")
            return redirect('home')
        if not isinstance(fname, str):
            messages.error(request, "First Name should be a string. Try again")
            return redirect('home')
        if not isinstance(lname, str):
            messages.error(request, "Last Name should be a string. Try again")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match. Try again")
            return redirect('home')

        # create User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your LCS account has been created successfully!")
        return redirect('home')

    else:
        return HttpResponse("404 not found!")

def handel_login(request):

    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request , user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')

        else:
            messages.error(request, "Invalid Credentials, Try Again")
            return redirect('home')
        
    return HttpResponse("404 not found!")
def handel_logout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out!")
    return redirect('home')

def success(request):
    return render(request, "success.html")

def cancel(request):
    return render(request, "cancel.html")


# stripe

stripe.api_key = settings.STRIPE_SECRET_KEY




def create_checkout_session_form(request):
    
    # Create a new Checkout Session
    # if request.method == 'POST':
    #     amount = int(request.POST.get('amount', 0))  # Assuming the amount is submitted via a form field
    #     session = create_checkout_session(request, amount)
    #     # Redirect the user to the Stripe Checkout page using the session URL
    #     return render(request, 'checkout.html', {'session': session})

    # return render(request, 'checkout_form.html')
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Donate for a Better Society',
                    },
                    'unit_amount': 100,  # Amount in cents
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('cancel')),
    )

    return redirect(session.url)

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')


def send_email_to_volunteers(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Retrieve all volunteers from the database
        volunteers = volunteer.objects.all()

        # Create a list of email tuples (subject, message, from_email, recipient_list)
        email_tuples = [(subject, message, 'ombhokare29@gmail.com', [volunteer.email]) for volunteer in volunteers]

        # Send the mass email
        send_mass_mail(email_tuples, fail_silently=False)

        messages.success(request, 'Emails sent successfully to all volunteers.')

    return render(request, 'send_email.html')