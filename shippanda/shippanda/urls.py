from django.conf.urls import patterns, include, url
from django.contrib import admin
from myapp.api import UserResource,AddressResource,OrderResource,ShipmentResource,XResource
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(AddressResource())
v1_api.register(OrderResource())
v1_api.register(ShipmentResource())
v1_api.register(XResource())



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shippanda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
