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
        if authorization_header is None or not isinstance(authorization_header, str):
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
        if not base64_authorization_header or not base64_authorization_header.startswith("Basic "):
            return None
        try:
            encoded = base64_authorization_header.split(" ")
            encoded_basic = encoded[1]
            decoded = base64.b64decode(encoded_basic).decode("utf-8")
            return decoded
        except Exception:
            return None
        
    
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> tuple[str, str]:
        """Extract the user credentials from the decoded base64 authorization header
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        credentials = decoded_base64_authorization_header.split(':')
    
    # Ensure the credentials list contains exactly two elements
        if len(credentials) != 2:
            return None, None
    
    # Return the email and password
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
    
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current authenticated user
        """
        authorization_header = self.authorization_header(request)
        if authorization_header is None:
            return None

        base64_authorization_header = self.extract_base64_authorization_header(authorization_header)
        if base64_authorization_header is None:
            return None

        decoded_base64_authorization_header = self.decode_base64_authorization_header(base64_authorization_header)
        if decoded_base64_authorization_header is None:
            return None
        
        user_email, user_pwd = self.extract_user_credentials(decoded_base64_authorization_header)
        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
