from django.urls import path, include
from apiapp import views


urlpatterns = [
    path("customers/", views.Customer_API.as_view(),),
]
