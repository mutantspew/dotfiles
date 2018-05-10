import os, shutil, subprocess, sys, urllib.request
import log
from log import LogLevel as ll # save some finger strokes

class Sublime(object):
  
  def __init__(self, log, sublconfig):
    super(Sublime, self).__init__()
    self.log = log
    self.sublconfig = sublconfig

  def check_installed(self, package):
    return shutil.which(package)

  def run(self):
    l = self.log # save some finger strokes

    l.print("\n\nSublime Config", ll.Info)

    installed = False; # don't do anything if it's not installed

    if(not self.check_installed(self.sublconfig['which_package'])): # not installed
      choice = input('Install Sublime? [y/n] ').lower()

      if(choice == 'y'):
        installed = self.install(self.sublconfig['package'])
    else:
      installed = True

    if(installed == True):
      self.check_package_control()
      self.copy_configs(self.sublconfig['config_path'])

    else: # not installed
      l.print("Sublime not installed, nothing done", ll.Warn)

    l.print("\n\n")

  def install(self, package):
    try:
      ret = subprocess.run(['sudo', 'apt-get', 'install', package], check = True)
    except subprocess.CalledProcessError as err:
      self.log.print("Error: {}".format(err), ll.Error) # an error occurred
    else:
      return True

  def check_package_control(self):
    l = self.log
    dest = os.path.expanduser("~/.config/sublime-text-3/Installed Packages/Package Control.sublime-package")

    l.print("Checking for Package Control", ll.Info)

    if(os.path.isfile(dest)): # package control exists
      l.print("Package Control exists", ll.Debug)
    else:
      l.print("Installing Package Control", ll.Info)

      source = "https://packagecontrol.io/Package%20Control.sublime-package"
      url = urllib.request.urlopen(source)

      with open(dest, 'b+w') as f:
        f.write(url.read())

      l.print("Package Control installed", ll.Info)

  def copy_configs(self, path):
    l = self.log
    source = os.path.abspath('subl-conf/')
    dest = os.path.expanduser(path)

    l.print("Copying configs", ll.Info)

    for file in os.listdir(source):
      f = source + '/' + file
      subprocess.run(['cp', f, dest], check = True)
      l.print("Copied file: {}".format(f), ll.Debug)

    l.print("Files Copied", ll.Info)
