import os, shutil, subprocess, sys

import log
from log import LogLevel as ll

try:
  import yaml
except OSError:
  print("pyyaml required. use pip to install")
  sys.exit()

class Config(object):
  """docstring for Config"""
  def __init__(self, log, filename):
    super(Config, self).__init__()
    self.log = log
    self.file = filename

  def open(self):
    try:
      self.log.print("Opening config file: {}".format(self.file), ll.Info
        )
      with open(self.file, 'r') as f:
        self.raw_data = yaml.load(f)
    except FileNotFoundError:
      self.log.print("{}: file not found".format(self.file), ll.Error)
      sys.exit()
    else:
      self.log.print("Config loaded", ll.Debug)

      self.get_root_keys()

  def get_root_keys(self):
    self.log.print("Getting keys", ll.Debug)
    self.root_keys = []

    for k, v in self.raw_data.items():
      self.root_keys.append(k)

    self.log.print("Retrieved all root keys: {}".format(keys), ll.Debug)

  def get_raw_data(self):
    self.log.print("Getting config raw data", ll.Debug)
    return self.raw_data
