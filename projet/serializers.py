from rest_framework import serializers
from .models import DocumentComparison

class DocumentComparisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentComparison
        fields = '__all__'
