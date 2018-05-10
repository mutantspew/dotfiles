import os, sys
import ssh
import log
from log import LogLevel as ll

class Git(object):
  """docstring for Git"""
  def __init__(self, log):
    super(Git, self).__init__()
    self.log = log
    
  def key(self):
    pass
