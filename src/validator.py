def is_valid_email(email: str) -> bool:
    if "@" not in email:
    return False  # Wrong indentation - AGENT SHOULD FIX THIS
    if "." not in email.split("@")[1]:
        return False
    return True

def is_positive(num: int) -> bool:
    return num > 0