# validators.py

from datetime import datetime

def validate_name(name):
    return name.strip() != ""


# Validação simples de e-mail
# Coerente com nível do projeto

def validate_email(email):

    return (

        "@" in email

        and "." in email

        and " " not in email

        and len(email) >= 5
    )

def validate_not_empty(value):
    return value.strip() != ""


def validate_numeric(value):
    return value.isdigit()


def validate_positive_number(value):
    return value.isdigit() and int(value) > 0


def validate_id(id):
    return (
        id.strip() != ""
        and id.isdigit()
        and id != "000"
    )

def validate_existing_id(id, valid_ids):
    return id in valid_ids

def validate_menu_option(option, valid_options):
    return option in valid_options

# Valida datas reais no formato DD/MM/AAAA

def validate_date(date):

    try:

        datetime.strptime(
            date,
            "%d/%m/%Y"
        )

        return True

    except ValueError:

        return False

def validate_float(value):
    try:
        return float(value) > 0

    except ValueError:
        return False