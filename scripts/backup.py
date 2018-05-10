import os, shutil, subprocess, sys

class Backup(object):
  """docstring for Backup"""
  def __init__(self, log):
    super(Backup, self).__init__()
    self.log = log
