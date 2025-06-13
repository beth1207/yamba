from datetime import timedelta
from django.utils import timezone
from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


class Job(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('filled', 'Filled'),
        ('cancelled', 'Cancelled'),
        ('expired', 'Expired'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    skills_required = models.CharField(max_length=200)
    expiry_date = models.DateTimeField(default=timezone.now() + timedelta(days=7))
    is_urgent = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        default=Decimal('0.00'),
    )

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_negotiable = models.BooleanField(default=False)

def is_expired(self):
        return timezone.now() > self.expiry_date
