import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

# Create your models here.

class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=32, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=128, null=False, blank=False)
    street_address2 = models.CharField(max_length=128, null=True, blank=True)
    city_town = models.CharField(max_length=128, null=False, blank=False)
    county_state = models.CharField(max_length=64, null=True, blank=True)
    postcode_zip = models.CharField(max_length=12, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    total_order = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    delivery_charge = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generates a random string
        """
        
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update total each time a line is added.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.delivery_charge = self.total_order * settings.DELIVERY_PERCENTAGE / 100
        self.grand_total = self.total_order + self.delivery_charge
        self.save()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)


      
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
