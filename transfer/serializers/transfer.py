from rest_framework import serializers

from transfer.models import Transfer


class TransferListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transfer

        fields = (
            "id",
            "product",
            "source_warehouse",
            "destination_warehouse",
            "quantity",
            "created_at",
        )


class TransferCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transfer

        fields = (
            "source_warehouse",
            "destination_warehouse",
            "product",
            "quantity",
            "notes",
        )