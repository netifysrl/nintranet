from django.db import models


# Create your models here.

class Customer(models.Model):
    
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    address3 = models.CharField(max_length=100, blank=True)
    zippostal = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    vat_number = models.CharField(max_length=25, blank=True)
    cod_rea = models.CharField(max_length=20, blank=True)
    email_bill = models.EmailField(blank=True)
    email_sales = models.EmailField(blank=True)
    email_tech = models.EmailField()
    email_generic = models.EmailField(blank=True)

    def __str__(self):
        return self.company

class CustomerContact(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    mobile_phome = models.CharField(max_length=15)
    contact_email = models.EmailField()
    note = models.CharField(max_length=1000)

    def __str__(self):
        return self.name +  " " + self.lastname

