from rest_framework import serializers


class KpiSerializer(serializers.Serializer):
    id = serializers.CharField()
    value = serializers.DecimalField(max_digits=14, decimal_places=0)
    change_percent = serializers.FloatField(allow_null=True)
    trend = serializers.ChoiceField(choices=["up", "down"], allow_null=True)


class MonthlyPointSerializer(serializers.Serializer):
    month = serializers.DateField()
    sales = serializers.DecimalField(max_digits=14, decimal_places=0)
    orders = serializers.IntegerField()


class TransactionSerializer(serializers.Serializer):
    id = serializers.CharField()
    party = serializers.CharField()
    description = serializers.CharField()
    date = serializers.DateField()
    amount = serializers.DecimalField(max_digits=14, decimal_places=0)
    direction = serializers.ChoiceField(choices=["in", "out"])
    status = serializers.CharField()


class TopProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    category = serializers.CharField(allow_null=True)
    amount = serializers.DecimalField(max_digits=14, decimal_places=0)
    share = serializers.FloatField()


class OverviewSerializer(serializers.Serializer):
    """Documents OverviewView's response shape for the OpenAPI schema — the
    view builds this dict by hand (it merges 4 selectors), so it isn't a
    GenericAPIView that spectacular can introspect automatically."""

    kpis = KpiSerializer(many=True)
    monthly_trend = MonthlyPointSerializer(many=True)
    recent_transactions = TransactionSerializer(many=True)
    top_products = TopProductSerializer(many=True)
