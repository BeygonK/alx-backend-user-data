#!/usr/bin/env python3
"""This module contains a class
that inherits from Auth class
"""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Inherits from Auth class
    and implements basic authentication
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns Base64 encoded authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        parts = authorization_header.split(' ')
        return parts[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """Decodes Base64 encoded authorization header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except ValueError:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str)-> (str, str):
        """Returns username and password from decoded Base64 encoded authorization header"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        parts = decoded_base64_authorization_header.split(':')
        if len(parts) != 2:
            return None, None
        return parts[0], parts[1]
