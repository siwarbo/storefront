from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerChoices()
    last_update=models.DateTimeField(auto_now=True)

class Customer(models.Model):
    MEMBERSHIP_BRONZE ='B'
    MEMBERSHIP_SILVER ='S'
    MEMBERSHIP_GOLD ='G'

    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    e_mail=models.EmailField(unique=True)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING='P'
    PAYMENT_STATUS_COMPLETE='C'
    PAYMENT_STATUS_FAILED='F'

    MEMBERSHIP_CHOICES=[
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed'),
    ]
    placed_at=models.DateField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=PAYMENT_STATUS_PENDING)