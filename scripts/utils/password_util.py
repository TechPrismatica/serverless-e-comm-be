import bcrypt


def encrypt_password(password: str) -> str:
    """Encrypts a password using bcrypt."""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed.decode()

def verify_password(password: str, hashed: str) -> bool:
    """Verifies a password against a bcrypt hash."""
    return bcrypt.checkpw(password.encode(), hashed.encode())
