'''
    This module creates a logger, it's designed as a singleton so that 
    there will only ever be one logger no matter how many times it's 
    created.

    This logger is also threadsafe for future proofing.
'''

import os
import logging
import logging.handlers
from typing import Optional
from threading import Lock


class Logger():
    '''
        This is a logger in the form of a singleton, the first initialization will
        instanciate the logger. Future instanciations will return the handle of the
        original instance.
    '''

    _instance = None
    _initialized: bool = False
    _instance_lock: Lock = Lock()
    _init_lock: Lock = Lock()
    _initialize_logger_lock: Lock = Lock()


    def __new__(cls, *args, **kwargs):
        '''
            Thread safe __new__ method that ensures creation of only 1 instance
            of the Logger class.
        '''

        with cls._instance_lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
                cls._instance._initialized = False
        return cls._instance


    def __init__(self, name='logger', log_file=None, level=logging.INFO, console=True):
        '''
            Initializes the Logger class with the settings that will be used for
            all loggers that are greated under it.

            Args:
                name (str): The name for the default logger, could be your application name
                log_file (str): The filename for your log file
                level (logging.LEVEL): The log level, this is overridden by env var LOG_LEVEL
                console (bool): To log to console, Default=True

            Returns:
                None
        '''

        with self._init_lock:
            if self._initialized:
                return
            self._initialized = True

            self.default_name: str = name
            self.log_file: Optional[str] = log_file
            self.console: bool = console
            self.loggers: dict = {}

            # Log level is determined foremost by the environment variable LOG_LEVEL
            if "LOG_LEVEL" in os.environ:
                self.level = getattr(logging, str(os.getenv("LOG_LEVEL")).strip().upper())
            else:
                self.level = level

            # Initialize the default logger
            self._initialize_logger(name)


    def _initialize_logger(self, name):
        '''
            Creates a named logger

            Args:
                name (str): Name of the logger, could be aplication name, network, filesysem, etc

            Returns:
                logger: A handle to the named logger
        '''

        if name in self.loggers:
            return self.loggers[name]

        while self._initialize_logger_lock:

            logger = logging.getLogger(name)

            logger.setLevel(self.level)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            if self.log_file is not None:
                file_handler = logging.FileHandler(self.log_file)
                file_handler.setLevel(self.level)
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)

            if self.console:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(self.level)
                console_handler.setFormatter(formatter)
                logger.addHandler(console_handler)

            self.loggers[name] = logger

            return logger

        # Fallback is to return the default logger if while loop condition is false
        return self.loggers[self.default_name]


    def get_logger(self, name=None):
        '''
            Returns the handle of the named logger.

            Args:
                name: str 

            Returns:
                logger: A handle to the named logger
        '''

        if name is None:
            name = self.default_name

        if name not in self.loggers:
            self._initialize_logger(name)

        return self.loggers[name]
