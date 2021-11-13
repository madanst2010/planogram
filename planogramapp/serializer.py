from django.db.models import fields
from django.db.models.base import Model
from planogramapp.models import PlanogramDetails, Planogram
from rest_framework import serializers
class PlanogramSerializer(serializers.ModelSerializer):
    def create(self, validata_data):
        return Planogram.objects.create(**validata_data)
    class Meta:
        model = Planogram
        fields = '__all__'
class PlanogramDetailSerializer(serializers.ModelSerializer):
    def create(self, validata_data):
        return PlanogramDetails.objects.create(**validata_data)
    class Meta:
        model = PlanogramDetails
        fields = '__all__'
    