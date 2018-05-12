import os, shutil, subprocess, sys

import log
from log import LogLevel as ll

import zsh, backup

class ZSH(object):
  """docstring for ZSH"""
  def __init__(self, log, zshconfig):
    super(ZSH, self).__init__()
    self.log = log
    self.config = zshconfig

  def run(self):
    l = self.log

    l.print("Checking if zsh is installed", ll.Debug)
    if(self.check_zsh_installed() is False):
      l.print("Not installed", ll.Debug)
      choice = input('Install Zsh? [y/n]').lower()

      if(choice == 'y'):
        self.install_zsh()
      else: # nothing left to do
        return

      # set zsh as the default
     self.self.set_zsh_default()

      if(self.check_oh_my_zsh_installed() is False):
        self.install_oh_my_Zsh()

    # backup zsh default configs
    self.backup_zsh_config()

    # link files
    self.link_zsh_config()

  def check_zsh_installed(self):
    self.log.print('Checking for Zsh', ll.Debug)
    return shutil.which('zsh')

  def check_oh_my_zsh_installed(self):
    pass

  def install_zsh(self):
    self.log.print('Installing Zsh', ll.Debug)
    try:
      ret = subprocess.run(['sudo', 'apt-get', 'install', 'zsh'], check = True)
    except subprocess.CalledProcessError as err:
      self.log.print("Error: {}".format(err), ll.Error) # an error occurred
    else:
      self.log.print('Zsh installed', ll.Debug)
      return True

  def set_zsh_default(self):
    self.log.print('Setting Zsh as the default shell', ll.Debug)
    try:
      ret = subprocess.run(['chsh', 'zsh'], check = True)
    except subprocess.CalledProcessError as err:
      self.log.print("Error: {}".format(err), ll.Error) # an error occurred
    else:
      return True

  def install_oh_my_Zsh(self):
    self.log.print('Installing Oh My Zsh', ll.Debug)
    args = ['sh', '-c', "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"]

    try:
      ret = subprocess.run(args, check = True)
    except subprocess.CalledProcessError as err:
      self.log.print("Error: {}".format(err), ll.Error) # an error occurred
    else:
      return True

  def backup_zsh_config(self):
    pass

  def link_zsh_config(self):
    pass
