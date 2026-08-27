from rest_framework import serializers

from apps.finance.models import Account, FinanceRecord
from apps.finance.services import finance_record_create


class AccountSerializer(serializers.ModelSerializer):
    last_activity = serializers.DateField(read_only=True)

    class Meta:
        model = Account
        fields = ["id", "account_type", "name", "balance", "last_activity"]
        read_only_fields = ["id", "balance"]  # balance only changes via finance_record_create


class FinanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceRecord
        fields = ["id", "description", "type", "category", "amount", "date", "account"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return finance_record_create(**validated_data)
