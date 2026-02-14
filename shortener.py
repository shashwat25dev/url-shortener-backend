from nanoid import generate
import os
from dotenv import load_dotenv

load_dotenv()

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
SHORT_CODE_LENGTH = int(os.getenv("SHORT_CODE_LENGTH", 7))

def generate_short_code() -> str:
    return generate(ALPHABET, SHORT_CODE_LENGTH)

def create_short_url(long_url: str) -> str:
    return generate_short_code()
