#!/usr/bin/env python3
"""This module contains class for
authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Class for authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the request requires authentication
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """Get authorization header from the request
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current authenticated user
        """
        return None
                