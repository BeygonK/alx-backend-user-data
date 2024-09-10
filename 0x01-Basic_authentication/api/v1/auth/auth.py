#!/usr/bin/env python3
"""This is a parent class
for authorization
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """This is a template for authorization"""
    def require_auth(self,
                     path: str,
                     excluded_paths: List[str]) -> bool:
        """checks if the paths is included"""
        return False

    def authorization_header(self, request=None) -> str:
        """extracts the authorization header from the request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns the current user from the authorization header"""
        return None
