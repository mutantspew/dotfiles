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
    self.log.print("git.key", ll.Debug)
    s = ssh.SSH(self.log)
    s.create_key('id_test4096', "4096", 'test')
