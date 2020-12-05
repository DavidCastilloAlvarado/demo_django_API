from django.urls import path, include
from apiapp import views

urlpatterns = [
    path("customers/", views.Rest_api_customers.as_view(),)
]
