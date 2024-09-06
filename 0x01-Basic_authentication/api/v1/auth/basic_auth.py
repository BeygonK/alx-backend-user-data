#!/usr/bin/env python3
"""This class implements
basic authentication
"""

import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import List, TypeVar


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
        
    
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract the user credentials from the decoded base64 authorization header
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        credentials = decoded_base64_authorization_header.split(':')
        if len(credentials) != 2:
            return None, None
        return credentials[0], credentials[1]
    
    
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Create a user object from the email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        user_list: List[User] = User.search({'email': user_email})
        if not user_list or len(user_list) == 0:
            return None
        user = user_list[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user