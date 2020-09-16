from .models import Flight, Booking
from .serializers import BookingListSerializers,FlightListSerializers
from rest_framework.generics import ListAPIView
from datetime import date as dates
from django.http import JsonResponse


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=(dates.today()))

    serializer_class = BookingListSerializers

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()

    serializer_class = FlightListSerializers
