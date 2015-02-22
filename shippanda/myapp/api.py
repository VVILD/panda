from tastypie.resources import ModelResource
from myapp.models import *
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.serializers import Serializer
from random import randint
import urllib2,urllib
import hashlib, random
import os
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authentication import ApiKeyAuthentication

class MultipartResource(object):
    def deserialize(self, request, data, format=None):
        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')

        if format == 'application/x-www-form-urlencoded':
            return request.POST

        if format.startswith('multipart'):
            data = request.POST.copy()
            data.update(request.FILES)

            return data

        return super(MultipartResource, self).deserialize(request, data, format)

class XResource(MultipartResource,ModelResource):
	C = fields.FileField(attribute="C", null=True, blank=True)
	class Meta:
		queryset = X.objects.all()
		resource_name = 'x'
		authorization= Authorization()
		always_return_data = True

	def hydrate(self, bundle):
		print bundle.request
		print bundle.data['Name']
		print bundle.data['C']
		return bundle

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		authorization= Authorization()
		always_return_data = True


class AddressResource(ModelResource):
	class Meta:
		queryset = Address.objects.all()
		resource_name = 'address'
		authorization= Authorization()
		always_return_data = True


class OrderResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user')
	pickup_address= fields.ForeignKey(AddressResource, 'pickup_address')
	class Meta:
		queryset = Order.objects.all()
		resource_name = 'order'
		authorization= Authorization()
		always_return_data = True

class ShipmentResource(MultipartResource,ModelResource):
	order=fields.ForeignKey(OrderResource, 'order')
	drop_address= fields.ForeignKey(AddressResource, 'drop_address')
	img = fields.FileField(attribute="img", null=True, blank=True)
	class Meta:
		queryset = Shipment.objects.all()
		resource_name = 'shipment'
		authorization= Authorization()
		always_return_data = True




