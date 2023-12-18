from .models import Accountability
from rest_framework import serializers

class AccountabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountability
        fields = '__all__'