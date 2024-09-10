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
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """extracts the authorization header from the request"""
        if request is None:
            return None
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns the current user from the authorization header"""
        return None
