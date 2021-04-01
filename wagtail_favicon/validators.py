from django.core.exceptions import ValidationError
import re


def validate_hex(value):
    matches = re.match(r'^#(?:[A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})$', value, re.I)

    if not matches:
        raise ValidationError('{} is not a valid hex color. e.g. #ABC123'.format(value))
