# custom_validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_password_contains_uppercase(password):
    if not any(char.isupper() for char in password):
        raise ValidationError(
            _("The password must contain at least one uppercase letter."),
            code='password_no_uppercase',
        )
