import re

from rest_framework import serializers


def bin_value_validator(value: str):
    if re.search(r"[^01]+|^0.+", value):
        raise serializers.ValidationError("Value format is invalid")


class CalculationSerializer(serializers.Serializer):
    first_value = serializers.CharField(
        validators=[bin_value_validator], max_length=20
    )
    second_value = serializers.CharField(
        validators=[bin_value_validator], max_length=20
    )
