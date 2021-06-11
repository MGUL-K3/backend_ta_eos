from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop("remove_fields", None)

        super().__init__(*args, **kwargs)
        if not remove_fields:
            return

        for field_name in remove_fields:
            self.fields.pop(field_name)

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Leave empty if no change needed",
        style={"input_type": "password", "placeholder": "Password"},
    )

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "name",
            "surname",
            "patronymic",
            "group",
        ]
