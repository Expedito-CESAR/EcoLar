# validação de dados centralizado, reutilizável.

# validação de nome
def validate_name(name):
    return name.strip() != ""

def validate_email(email):
    return "@" in email and "." in email