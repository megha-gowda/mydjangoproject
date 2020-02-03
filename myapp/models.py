from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	cpassword=models.CharField(max_length=100)
	contact=models.CharField(max_length=100)
	status=models.CharField(max_length=100,default="inactive")

	def __str__(self):
		return self.first_name+" "+self.last_name

class Event(models.Model):
	CHOICES = (
        ("Sports",'Sports'),
        ("Politics",'Politics'),
        ("Bollywood",'Bollywood'),)
	event_category=models.CharField(max_length=50,choices=CHOICES,default="")
	event_name=models.CharField(max_length=50)
	event_image=models.ImageField(upload_to='images/')
	event_price=models.IntegerField(default=0)
	event_desc=models.TextField()

	def __str__(self):
		return self.event_name
class Contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	mobile=models.CharField(max_length=200)
	remarks=models.TextField()

	def __str__(self):
		return self.name

class BookEvent(models.Model):
	uid=models.ForeignKey(User,on_delete=models.CASCADE)
	eid=models.ForeignKey(Event,on_delete=models.CASCADE)
	booking_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.uid.first_name