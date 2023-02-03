from rest_framework import serializers
from .models import AdvertData

class AdvertDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertData
        fields = "__all__"