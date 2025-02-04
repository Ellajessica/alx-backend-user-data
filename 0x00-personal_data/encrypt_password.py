#!/usr/bin/env python3
"""module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hhes a password using a random salt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Ccks is a hashed password was formed from the given password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
