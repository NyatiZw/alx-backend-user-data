#!/usr/bin/env python3
"""
SQLAlchemy model for users database

Attributes:
    -ID: Integer primary key
    -EMAIL: non-nullable string
    -HASHED_PASSWORD: non-nullable string
    -SESSION_ID: nullable string
    -RESET_TOKEN: nullable string
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional


Base = declarative_base()


class User(Base):
    __tablename__: str = 'users'

    id: Column = Column(Integer, primary_key=True)
    email: Column = Column(String(250), nullable=False)
    hashed_password: Column = Column(String(250), nullable=False)
    session_id: Column = Column(String(250), nullable=True)
    reset_token: Column = Column(String(250), nullable=True)
