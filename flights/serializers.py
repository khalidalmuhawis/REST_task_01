from .models import Flight, Booking
from rest_framework import serializers


class FlightListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id','destination','time','price']


class BookingListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight','date','id']
