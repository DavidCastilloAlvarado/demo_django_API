from django.urls import path, include
from webapp.views import view_customers

urlpatterns = [
    path("", view_customers)
]
