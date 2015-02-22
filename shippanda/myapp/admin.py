from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	search_fields=['phone','name']
	list_display = ('phone','name','otp','apikey','referral_code')
	list_editable = ('name',)


admin.site.register(User,UserAdmin)

admin.site.register(Address)

class OrderAdmin(admin.ModelAdmin):
	search_fields=['phone','name']
	list_display = ('tracking_no','mapped_tracking_no','date','time','status')
	list_editable = ('status',)


admin.site.register(Order,OrderAdmin)

class ShipmentAdmin(admin.ModelAdmin):
	list_display = ('img','category','drop_phone','drop_name','drop_address')

admin.site.register(Shipment,ShipmentAdmin)

admin.site.register(X)
