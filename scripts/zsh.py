import os, shutil, subprocess, sys

import log
from log import LogLevel as ll

import link, backup

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
    self.set_zsh_default()

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
    self.log.print('Checking for Oh My Zsh', ll.Debug)

    if(os.path.exists(os.path.expanduser('~/.oh-my-zsh'))):
      self.log.print('Oh-My-Zsh installed', ll.Debug)
      return True
    else:
      self.log.print('Oh-My-Zsh not installed', ll.Debug)
      return False

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
      # ret = subprocess.run('/bin/bash -c "chsh -s "$(which zsh)""', shell = True)
      ret = subprocess.run(['chsh', '-s', shutil.which('zsh')])
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
    self.log.print('Backing up zsh config', ll.Info)

    b = backup.Backup(log)

    self.log.print('Done', ll.Debug)

  def link_zsh_config(self):
    self.log.print('Linking zsh config', ll.Info)

    l = link.Link(log)

    self.log.print('Done', ll.Debug)
