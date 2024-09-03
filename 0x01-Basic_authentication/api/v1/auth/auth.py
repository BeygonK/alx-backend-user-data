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
        if path is None:
            return True
        if not excluded_paths or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'
        if path in excluded_paths:
            return False
        return True
    
    def authorization_header(self, request=None) -> str:
        """Get authorization header from the request
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current authenticated user
        """
        return None
                