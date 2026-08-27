from rest_framework import serializers

from apps.production.models import ProductionLine, QualityCheck


class ProductionLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLine
        fields = ["id", "name", "product", "capacity", "efficiency", "status"]
        read_only_fields = ["id"]


class QualityCheckSerializer(serializers.ModelSerializer):
    inspector_name = serializers.CharField(source="inspector.full_name", read_only=True, default=None)

    class Meta:
        model = QualityCheck
        fields = ["id", "line", "product", "date", "inspector", "inspector_name", "result", "notes"]
        read_only_fields = ["id"]
