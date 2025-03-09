from django.db import models
from users.models import Customer



class Product(models.Model):
        customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
        product_name = models.CharField(max_length=255)
        model_number = models.CharField(max_length=100)
        purchase_date = models.DateField()
        warranty_status = models.IntegerField(help_text="Warranty period in months")
        def __str__(self):
            return self.product_name