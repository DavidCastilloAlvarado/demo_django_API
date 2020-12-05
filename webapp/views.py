from django.shortcuts import render
from datetime import datetime
# Create your views here.


def view_customers(request):
    fecha_actual = datetime.now()
    return render(request, "home.html", {"timenow": fecha_actual})
