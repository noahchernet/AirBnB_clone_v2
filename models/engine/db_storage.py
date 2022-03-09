#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from ..amenity import Amenity
from ..base_model import BaseModel, Base
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State
from ..user import User
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database."""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://'
                                      '{}:{}@{}:3306/{}'.format(
                                          getenv('HBNB_MYSQL_USER'), getenv(
                                              'HBNB_MYSQL_PASSWORD'),
                                          getenv('HBNB_MYSQL_HOST'), getenv(
                                              'HBNB_MYSQL_DB')
                                      ), pool_pre_ping=True)
        # self.__session = sessionmaker(bind=self.__engine)

        if getenv('HBNB_ENV') == 'test':
            metadata = MetaData(self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dict = {}
        if cls:
            cls_objs = self.__session.query(cls).all()
            for obj in cls_objs:
                dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
            return dict

        cls_objs = self.__session.query().all()
        for obj in cls_objs:
            dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return dict

    def new(self, obj):
        """Adds new object to storage's session.
        But it doesn't save it yet."""
        self.__session.add(obj)

    def save(self):
        """Saves session's added (and removed) objects to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        self.__session.delete(obj)

    def reload(self):
        """Loads all the objects stored in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__session, expire_on_commit=False))
