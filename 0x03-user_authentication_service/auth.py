#!/usr/bin/env python3
"""
Authentication
"""
import bcrypt


def _hash_password(password) -> bytes:
    """Hash a password using bcrypt
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)