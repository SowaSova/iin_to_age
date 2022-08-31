from django.core.exceptions import ValidationError
from django.db import models


def validate_length(obj, value=12):
    if len(str(obj)) < value:
        raise ValidationError("Not enough symbols(need 12).")


class Person(models.Model):
    iin = models.CharField(
        max_length=12,
        verbose_name="IIN",
        unique=True,
        validators=[validate_length],
    )
