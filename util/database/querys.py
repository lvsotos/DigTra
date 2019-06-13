# -*- coding: utf-8 -*-

import logging
from util import Basics
from util.database.connection import MysqlConn
from mysql.connector import Error

class DBQuerys:

    def __init__(self):
        self._basics = Basics()
        self.__connect = MysqlConn()

        self.__repo_name = "repo_name"
        self.__gestor = "gestor_responsable"
        self.__tipo_repo = "tipo_repositorio"

    def search_all_repos(self):

        cnx, cursor = self.__connect.connect()

        try:
            _message = {}

            query = "SELECT " \
                    "repositorios.uuid_repo, " \
                    "repositorios.repository_name, " \
                    "repositorios.gestor_responsable, " \
                    "repositorios.tipo_repositorio " \
                    "FROM vasallo.repositorios; "
            cursor.execute(query)

            _data = cursor.fetchall()

            for dat in _data:

                _message[dat[0]] = {self.__repo_name: dat[1],
                                    self.__gestor: dat[2],
                                    self.__tipo_repo: dat[3]}
            return _message

        except Exception as ex:
            logging.info(ex)
        except IOError as ex1:
            logging.info(ex1)
        finally:
            cursor.close()
            cnx.close()

    def contar_tipo_repositorios(self):
        cnx, cursor = self.__connect.connect()
        try:
            _message = {}

            query = "SELECT repositorios.tipo_repositorio, " \
                    "COUNT(repositorios.repository_name) AS tipos_de_repositorios " \
                    "FROM vasallo.repositorios GROUP BY repositorios.tipo_repositorio;"

            cursor.execute(query)
            data = cursor.fetchall()

            for dat in data:
                _message[dat[0]] = dat[1]

            return _message

        except Exception as ex:
            logging.info(ex)

        finally:
            cursor.close()
            cnx.close()


    def contar_all_repos(self):
        cnx, cursor = self.__connect.connect()
        try:
            query = "select count(repositorios.repository_name) from vasallo.repositorios;"
            cursor.execute(query)

            return cursor.fetchone()

        except Exception as ex:
            logging.info(ex)
        finally:
            cursor.close()
            cnx.close()


