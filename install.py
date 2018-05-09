#!/usr/bin/env python3

import os, sys, shutil, subprocess
from argparse import ArgumentParser

sys.path.insert(0, 'scripts')
import log
from log import LogLevel

try:
  import yaml
except OSError:
  print("pyyaml required. use pip to install")
  sys.exit()

log = log.Log()

def add_arg_options(parser):
  parser.add_argument('-c', '--config-file', nargs = 1, dest = 'config_file',
                      help = 'run commands given in CONFIGFILE', metavar = 'CONFIGFILE', #required = True,
                      default = 'config.yaml')

def read_config(config_file):
  try:
    with open(config_file, "r") as f:
      data = yaml.load(f)
  except FileNotFoundError:
    log.print("{}: file not found".format(config_file), LogLevel.Error)
    sys.exit()

  return data


def backup_files(list):
  files = list.split(' ')
  dst = os.path.expanduser("~") + "/.backup-dotfiles"

  log.print("{} Exits? {}".format(dst, os.path.exists(dst)), LogLevel.Debug)

  # check if there is already a backup dir, if not make it
  if( not os.path.exists(dst)):
    log.print("creating directory " + dst, LogLevel.Info)
    os.makedirs(dst)

  #loop through our files, if it exits move it to the backup directory
  for f in files:
    path = os.path.expanduser("~") + "/" + f

    if(os.path.isfile(path)): #exits
      try:
        shutil.move(path, dst)
      except Exception as e:
        log.print("Skipped file: {}".format(path), LogLevel.Warn)
      else:
        log.print("Moving {} to {}".format(path, dst), LogLevel.Info)


def install_files(list):
  for v in list:
    if shutil.which(v) is None: # package doesn't exist
      print("Installing: {}".format(v))

      # install the package
      try:
        ret = subprocess.run(['sudo', 'apt-get', 'install', v], check = True)
      except subprocess.CalledProcessError as err:
        log.print("Error: {}".format(err), LogLevel.Error) # an error occured
      else:
        log.print("{} installed".format(v), LogLevel.Info) # everything went well, package installed

    else: # package is already installed
      log.print("{} is already installed".format(v), LogLevel.Info)


def link_files(list):
  for k, v in list.items():
    if(os.path.exists(v)): # if we have a config file for it
      dest_file = os.path.expanduser(k)

      if(not os.path.islink(dest_file)): # we don't need to link if it already is
        source_file = os.path.abspath(v)
        
        try:
          os.symlink(source_file, dest_file)
        except OSError as e:
          log.print("Failed to link file: {}".format(dest_file), LogLevel.Error)
        else:
          log.print("Linked file: {} -> {}".format(dest_file, source_file), LogLevel.Info)
      else: #
        log.print("{} already linked".format(dest_file), LogLevel.Warn)
    

def check_root():
  if(os.getuid() != 0):
    log.print("must be root to run", LogLevel.Error)
    sys.exit()

def main():
  #check to see if we are root first
  check_root()

  try:
    # create the parser and add our options to look for
    parser = ArgumentParser()
    add_arg_options(parser)

    # parse the arguments
    options = parser.parse_args()

    # read our config file
    data = read_config(options.config_file)

    for k, v in data.items():
      if(k == 'backup'):
        backup_files(v)
        # pass

      elif (k == 'install'):
        install_files(v)
        pass

      elif (k == 'link'):
        link_files(v)

      else:
        pass

  except OSError:
    log.print("FIALED SPLATESDSDEHLKJA:HFU*IH", LogLevel.Error)


main()

