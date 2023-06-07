#!/usr/bin/env python3
"""  This User session module
"""
from models.base import Base


class UserSession(Base):
    """ This UserSession class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ This Initialize a UserSession instance
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
