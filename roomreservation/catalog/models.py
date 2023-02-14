from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class RentalPlace(models.Model):
    """Model representing an hotel."""
    name = models.CharField(max_length=200, help_text="Enter the name of the rental place")
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True)
    street = models.CharField(max_length=200, help_text="Enter the name of the street where the place is located")
    city = models.CharField(max_length=50, help_text="Enter the name of the city where the place is located")
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the place")

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Room(models.Model):
    """Model representing a room."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular room accross the reservation website")
    rental_place = models.ForeignKey('RentalPlace', on_delete=models.RESTRICT, null=True)
    due_back = models.DateField(null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True, help_text="Enter the cost of the room for one night")
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_premium = models.BooleanField(help_text="If the room is for premium clients")
    

    RESERVATION_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'Booked'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=RESERVATION_STATUS,
        blank=True,
        default='d',
        help_text='Room availability')

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.rental_place.name)

class Owner(models.Model):
    """Model representing an owner."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True, help_text='000-000-0000 (Without the dashes)')

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)
