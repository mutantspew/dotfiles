import os, sys
from enum import Enum

class Color:
  Default = '\x1b[39m'

  Blue = '\x1b[34m'
  Green = '\x1b[32m'
  Red = '\x1b[31m'
  Yellow = '\x1b[33m'
  
  EndColor = '\x1b[0m'

class LogLevel(Enum):
   Info = 0
   Debug = 1
   Warn = 2
   Error = 3

class Log(object):
  """docstring for Log"""
  def __init__(self):
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
    elif(level == LogLevel.Debug):
      self._print_debug(msg)
    else:
      print(msg)

  def _print_info(self, msg):
    print(Color.Default + msg + Color.EndColor)

  def _print_debug(self, msg):
    print(Color.Blue + msg + Color.EndColor)

  def _print_error(self, msg):
    print(Color.Red + msg + Color.EndColor)

  def _print_warn(self, msg):
    print(Color.Yellow + msg + Color.EndColor)
