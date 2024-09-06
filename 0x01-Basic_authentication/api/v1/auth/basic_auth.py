#!/usr/bin/env python3
"""This class implements
basic authentication
"""

import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentication class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extract the base64 encoded authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        basic = authorization_header.split(' ')
        if len(basic) != 2:
            return None
        return basic[1]


    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decode the base64 encoded authorization header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None