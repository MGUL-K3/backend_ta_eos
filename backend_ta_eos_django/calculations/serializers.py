from rest_framework import serializers
import re


def bin_value_validator(value: str):
    if re.search(r"[^01]+", value):
        raise serializers.ValidationError("Value is invalid")


class CalculationSerializer(serializers.Serializer):
    first_value = serializers.CharField(validators=[bin_value_validator], max_length=20)
    second_value = serializers.CharField(
        validators=[bin_value_validator], max_length=20
    )
