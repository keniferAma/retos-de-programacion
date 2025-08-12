from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta

SECRET_KEY = "SECR3T"
ALGORITHM = "HS256"

def token_generator(user: str):
    payload = {
        "sub": user,
        "exp": datetime.now(timezone.utc) + timedelta(hours=22)
    }

    try:
        return jwt.encode(payload, SECRET_KEY, ALGORITHM)
        
    except JWTError as e:
        print(f"error {e}")

print(token_generator('kenifer'))


