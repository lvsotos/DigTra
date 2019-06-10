import logging
import os
from configparser import ConfigParser

class Basics:

    def __init__(self):

        logging.basicConfig(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'util_log.txt'))