import os, shutil, subprocess, sys

import zsh, backup

class ZSH(object):
  """docstring for ZSH"""
  def __init__(self, log, zshconfig):
    super(ZSH, self).__init__()
    self.log = log
    self.config = zshconfig

  def run(self):
    pass

  def check_zsh_installed(self):
    pass

  def check_oh_my_zsh_installed(self):
    pass

  def install_zsh(self):
    pass

  def set_zsh_default(self):
    pass

  def install_oh_my_Zsh(self):
    pass

  def backup_zsh_config(self):
    pass

  def link_zsh_config(self):
    pass
