import os, sys
from enum import Enum

class LogLevel(Enum):
   Info = 0
   Debug = 1
   Warn = 2
   Error = 3

class Log(object):
  """docstring for Log"""
  def __init__(self, arg):
    # super(Log, self).__init__()
    # self.arg = arg
    pass

  def print(self, msg, level = LogLevel.Info):
    if(level == LogLevel.Info):
      self._print_info(msg)
    elif(level == LogLevel.Warn):
      self._print_warn(msg)
    elif(level == LogLevel.Error):
      self._print_error(msg)
    else:
      print(msg)

  def _print_info(self, msg):
    print(msg)

  def _print_error(self, msg):
    print(msg)

  def _print_warn(self, msg):
    print(msg)
