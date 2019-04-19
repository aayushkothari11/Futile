from django.conf.urls import url
from .views import *
from payment import views

app_name = "payment"

urlpatterns = [
    url(r'^payment/$', views.payment, name="payment"),
    url(r'^payment/success$', views.payment_success, name="payment_success"),
    url(r'^payment/failure$', views.payment_failure, name="payment_failure"),
]
