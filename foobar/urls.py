from django.conf.urls import url, include
from foobar import views
from .views import TabDetail, TabList
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tablist', views.TabList, base_name='foo')
router.register(r'tab', views.TabDetail)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'pin/(?P<login>.+)/$', views.Pin.as_view())
]