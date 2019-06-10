# -*- coding: utf-8 -*-

import logging
import mysql.connector
import os
from util import Basics
from configparser import ConfigParser


class MysqlConn:

    def __init__(self):
        self._basics = Basics()
        self.__config = ConfigParser()
        self.__cfg_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.cfg')
        self.__config.read(self.__cfg_file)

    def connect(self):

        try:
            cnx = mysql.connector.connect(user=self.__config.get('DATABASE', 'USER'),
                                          password=self.__config.get('DATABASE', 'PWD'),
                                          host=self.__config.get('DATABASE', 'ENAP_DB'))

            cursor = cnx.cursor()
            return cnx, cursor

        except Exception as ex:
            logging.info(ex)