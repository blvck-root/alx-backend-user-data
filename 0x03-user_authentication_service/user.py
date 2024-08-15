#!/usr/bin/env python3
"""Create SQL Alchemy User model.
"""
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# create engine
engine = create_engine('sqlite:///:memory:', echo=True)

# maintains a catalog of classes and tables
Base = declarative_base()


class User(Base):
    """
    User model defines users table details.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
