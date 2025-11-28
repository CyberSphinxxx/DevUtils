import re

def is_valid_email(email):
    """
    Validates an email address using a regular expression.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    emails = [
        "test@example.com",
        "invalid-email",
        "user.name+tag@domain.co.uk",
        "user@sub.domain.com"
    ]
    for email in emails:
        print(f"{email}: {is_valid_email(email)}")
