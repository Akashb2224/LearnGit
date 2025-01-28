def validate_email(email):
    special = "!@#$%^&*"
    if len(email) >= 10:
        return True
    for char in email:
        if char in special:
            return True
        else:
            False
        
    