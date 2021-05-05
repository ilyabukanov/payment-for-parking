from rest_framework import serializers

from .models import Parking

class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parking
        fields = ('adress', 'starttime','endtime','minimaltimeforpayment','price','numberofavailableseats','tickets')