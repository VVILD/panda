from django.db import models
from django.core.validators import RegexValidator
import hashlib






class User(models.Model):
	phone_regex = RegexValidator(regex=r'^[0-9]*$', message="Phone number must be entered in the format: '999999999'. Up to 12 digits allowed.")
	phone = models.CharField(validators=[phone_regex],max_length = 12,primary_key=True)
	name = models.CharField(max_length = 10)
	password=models.CharField(max_length = 300)
	email = models.EmailField(max_length = 75,null=True,blank =True)
	otp=models.IntegerField(null=True,blank=True)
	apikey= models.CharField(max_length = 100,null=True,blank=True)
	referral_code= models.CharField(max_length = 50,null=True,blank=True)
	def save(self, *args, **kwargs):
		if self.password:
			algo='sha1'
			salt='crawLINGINmySKin'
			hsh = hashlib.sha224(algo+salt).hexdigest()
			self.password=hsh
		super(User, self).save(*args, **kwargs)

	def __unicode__(self):
		return str(self.name)

class Address(models.Model):
	flat_no=models.CharField(max_length = 100)
	city=models.CharField(max_length = 50)
	state=models.CharField(max_length = 50)
	pincode=models.CharField(max_length =30)
	country=models.CharField(max_length =30)
	def __unicode__(self):
		return str(self.flat_no)

class Order(models.Model):
	tracking_no=models.AutoField(primary_key=True)
	mapped_tracking_no=models.CharField(max_length = 10)
	date=models.DateField(null=True,blank =True)
	time=models.TimeField(null=True,blank =True)
	pickup_address=models.ForeignKey(Address)
	user=models.ForeignKey(User)
	tracking_data=models.CharField(max_length = 10)
	status=models.CharField(max_length=1,
									  choices=(('P','pending') ,('C','complete'),),
									  blank=True , null = True)
	cost=models.CharField(max_length = 10,null=True ,blank=True)
	paid=models.CharField(max_length=1,
									  choices=(('Y','yes') ,('N','no'),),
									  blank=True , null = True)

	cancelled=models.CharField(max_length=1,
									  choices=(('Y','yes') ,('N','no'),),
									  default='N')



class Shipment(models.Model):
	img=models.ImageField(upload_to = 'shipment/')	
	category=models.CharField(max_length=1,
									  choices=(('P','premium') ,('R','regular'),),
									  blank=True , null = True)
	drop_name=models.CharField(max_length = 10,null=True)
	phone_regex = RegexValidator(regex=r'^[0-9]*$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	drop_phone = models.CharField(validators=[phone_regex],max_length =12,null=True)
	drop_address=models.ForeignKey(Address,null=True)
	order=models.ForeignKey(Order,null=True)



class X(models.Model):
    Name = models.CharField(max_length = 100)
    C=models.ImageField(upload_to = 'shipment/')
    order=models.ForeignKey(Order,null=True)





