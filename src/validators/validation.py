from validate_email import validate_email
from password_validator import PasswordValidator


def password_validate(password: str) -> bool:
    schema = PasswordValidator()
    schema.has().uppercase().has().lowercase().has().digits().has().no().spaces().has().symbols()
    return schema.validate(password)


def email_validate(email: str) -> bool:
    return validate_email(email)

