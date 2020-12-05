from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    latitude = models.DecimalField(
        decimal_places=7, max_digits=15, default=-11.897072)
    longitude = models.DecimalField(
        decimal_places=7, max_digits=15, default=-77.0312574)

    def __str__(self):
        return self.first_name
