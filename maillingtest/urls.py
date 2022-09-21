from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from messageapp.views import ClientViewSet, MailingViewSet, Text_MessageViewSet



router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'textmessages', Text_MessageViewSet)
router.register(r'mailings', MailingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include("rest_framework.urls", namespace="rest_framework")),
]
