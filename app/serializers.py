from rest_framework import serializers
from .models import WalletKey















class WalletKeySerializer(serializers.ModelSerializer):


    class Meta:

        model = WalletKey
        fields = '__all__'