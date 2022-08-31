from datetime import datetime as dt

from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Person


class PersonaSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ("iin", "age")
        lookup_field = "iin"

    def validate_iin(self, value):
        if not value.isdigit():
            raise ValidationError("Only digits!")
        return value

    def get_age(self, obj):
        current_day = dt.now().day
        current_month = dt.now().month
        current_year = dt.now().year
        birth_day = int(obj.iin[4:6])
        birth_month = int(obj.iin[2:4])
        birth_year = int(obj.iin[0:2])
        age = (current_year - birth_year) % 100
        if (
            birth_month > current_month
            or current_month == birth_month
            and current_day < birth_day
        ):
            age -= 1
        return age
