from django.db import models

# Create your models here.
class Order(models.Model):
    customer_name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    address=models.TextField()
    products=models.TextField()
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    utr_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    payment_status = models.CharField(
        max_length=30,
        default="Pending"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (self.customer_name)