#!/usr/bin/env python3
"""
This SessionAuth module for the API
"""
from uuid import uuid4

from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """This A session auth class to manage the API authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """This Creates a Session ID for a user_id"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """This Returns a User ID based on a Session ID"""
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """This Returns a User instance based on a cookie value"""
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """This es the user session / logout"""
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if not session_cookie:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if not user_id:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
