#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import logging
import sys
from logging.handlers import RotatingFileHandler

try:
    LOG_FILENAME = os.path.splitext(__file__)[0] + ".log"
except:
    LOG_FILENAME = __file__ + ".log"

__header__ = "[Unit No.{}] [Unit Level{}] [Input1:{}] [Input2:{}] [Input3:{}] [Input4:{}] [Input5:{}] [Input6:{}] [Input7:{}] [Output1:{}] [Output2:{}] [Output3:{}] [Output4:{}] [Output5:{}] [Output6:{}] [Output7:{}]" 

class Singleton(object):
    """
    Singleton interface:
    """
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        pass

class LoggerManager(Singleton):
    """
    Logger Manager.
    Handles all logging files.
    """
    def init(self, loggername):
        self.logger = logging.getLogger(loggername)
        rhandler = None
        try:
            rhandler = RotatingFileHandler(
                    LOG_FILENAME,
                    mode='a',
                    maxBytes = 10 * 1024 * 1024,
                    backupCount=5
                )
        except:
            raise IOError("Couldn't create/open file \"" + \
                          LOG_FILENAME + "\". Check permissions.")

        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            fmt = '[%(filename)s:%(lineno)d] %(message)s'
 #           datefmt = '%F %H:%M:%S'
        )
        rhandler.setFormatter(formatter)
        self.logger.addHandler(rhandler)

    def debug(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        if len(msg) == 16:
            self.logger.debug(__header__.format(msg[0],msg[1],msg[2],msg[3],msg[4],msg[5],msg[6],msg[7],msg[8],msg[9],msg[10],msg[11],msg[12],msg[13],msg[14],msg[15]))
        elif type(msg) == str:
            self.logger.debug(msg)
        else:
            self.logger.debug("Error")
    def error(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.error(msg)

    def info(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.info(msg)

    def warning(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.warning(msg)

class Logger(object):
    """
    Logger object.
    """
    def __init__(self, loggername="root"):
        self.lm = LoggerManager(loggername) # LoggerManager instance
        self.loggername = loggername # logger name

    def debug(self, msg):
        self.lm.debug(self.loggername, msg)

    def error(self, msg):
        self.lm.error(self.loggername, msg)

    def info(self, msg):
        self.lm.info(self.loggername, msg)

    def warning(self, msg):
        self.lm.warning(self.loggername, msg)

if __name__ == '__main__':

    logger = Logger()
    msg = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    logger.debug(msg)
    logger.debug("this testname.")
