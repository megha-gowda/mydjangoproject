from django.shortcuts import render,get_object_or_404
from .models import User,Event,Contact,BookEvent
from django.core.mail import send_mail
import random
from django.conf import settings
# Create your views here.
def index(request):
	return render(request,'myapp/index.html')
def sports(request):
	sports=Event.objects.filter(event_category="Sports")
	return render(request,'myapp/sports.html',{'sports':sports})
def politics(request):
	politics=Event.objects.filter(event_category="Politics")
	return render(request,'myapp/politics.html',{'politics':politics})
def bollywood(request):
	bollywood=Event.objects.filter(event_category="Bollywood")
	return render(request,'myapp/bollywood.html',{'bollywood':bollywood})
def contact(request):
	return render(request,'myapp/contact.html')
def signup(request):
	return render(request,'myapp/signup.html')
def login(request):
	return render(request,'myapp/login.html')
def signup_user(request):
	if request.method=="POST":
		error=""
		first_name=request.POST["first_name"]
		last_name=request.POST["last_name"]
		email=request.POST["email"]
		password=request.POST["password"]
		cpassword=request.POST["cpassword"]
		contact=request.POST["contact"]

		user=User.objects.filter(email=email)
		if user:
			error="This email id is already registered with us."
			return render(request,'myapp/signup.html',{'error':error})
		else:
			if password==cpassword:
				User.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,cpassword=cpassword,contact=contact)
				rec=[email,]
				subject="OTP For Successfull Registration"
				otp=random.randint(1000,9999)
				message="Your OTP For Registration Is "+str(otp)
				email_from = settings.EMAIL_HOST_USER
				send_mail(subject, message, email_from, rec)
				return render(request,'myapp/otp.html',{'email':email,'otp':otp})
			else:
				error="Password and Confirm Password Not Matched"
				return render(request,'myapp/signup.html',{'error':error})
def login_user(request):
	if request.method=="POST":
		error=""
		email=request.POST["email"]
		password=request.POST["password"]

		try:
			user=User.objects.get(email=email,password=password)

			if user:
				if user.status=="active":
					request.session["first_name"]=user.first_name
					request.session["userpk"]=user.pk
					return render(request,'myapp/index.html')
				else:
					error="Your Status Is Still Not Active."
					return render(request,"myapp/login.html",{'error':error})
		except:
			error="Your Email or Password is Incorrect"
			return render(request,'myapp/login.html',{'error':error})
def logout(request):
	try:
		if request.session["first_name"]:
			del request.session["first_name"]
			del request.session["userpk"]
			return render(request,'myapp/index.html')
	except:
		return render(request,'myapp/index.html')

def validate_otp(request):
	email=request.POST["email"]
	otp=request.POST["otp"]
	e_otp=request.POST["e_otp"]

	print("OTP : ",otp)
	print("E_OTP : ",e_otp)

	if otp==e_otp:
		print("If")
		user=User.objects.get(email=email)
		user.status="active"
		user.save()
		return render(request,"myapp/login.html")
	else:
		print("else")
		return render(request,"myapp/login.html")
def detail(request,pk):
	event=get_object_or_404(Event,pk=pk)
	return render(request,'myapp/event_details.html',{'event':event})
def query(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		mobile=request.POST["mobile"]
		remarks=request.POST["remarks"]
		Contact.objects.create(name=name,email=email,mobile=mobile,remarks=remarks)
		msg="Contact Saved Successfully. Get Back To You Very Soon"
		return render(request,'myapp/contact.html',{'msg':msg})
def book_event(request,pk1,pk2):
	user=User.objects.get(pk=pk1)
	event=Event.objects.get(pk=pk2)
	BookEvent.objects.create(uid=user,eid=event)
	msg="Your Event Booked Successfully."
	return render(request,'myapp/index.html',{'msg':msg})

def mybooking(request):
	userpk=request.session['userpk']
	myevent=BookEvent.objects.filter(uid=userpk)
	return render(request,'myapp/mybooking.html',{'myevent':myevent})

def cancel_booking(request,pk):
	myevent=get_object_or_404(BookEvent,pk=pk)
	myevent.delete()
	userpk=request.session['userpk']
	myevent=BookEvent.objects.filter(uid=userpk)
	return render(request,'myapp/mybooking.html',{'myevent':myevent})
