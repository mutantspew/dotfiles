#!/usr/bin/env python3

import os, sys, shutil
from argparse import ArgumentParser
#from .config import ConfigReader, ReaderError

try:
  import yaml
except OSError:
  print("pyyaml required. use pip to install")
  os.exit()


def add_arg_options(parser):
  parser.add_argument('-c', '--config-file', nargs = 1, dest = 'config_file',
                      help = 'run commands given in CONFIGFILE', metavar = 'CONFIGFILE', required = True,
                      default = 'config.yaml')

def read_config(config_file):
  with open(config_file, "r") as f:
    data = yaml.load(f)

  return data


def backup_files(list):
  files = list.split(' ')
  dst = os.path.expanduser("~") + "/.backup-dotfiles"

  print (dst)
  print (os.path.exists(dst))
  # check if there is already a backup dir, if not make it
  if( not os.path.exists(dst)):
    print("creating directory " + dst)
    os.makedirs(dst)

  #loop through our files, if it exits move it to the backup directory
  for f in files:
    path = os.path.expanduser("~") + "/" + f

    if(os.path.isfile(path)): #exits
      print("Moving " + path + " to " + dst)
      shutil.move(path, dst)


def install_files(list):
  #for v in list.items():
   # print (v)
  pass

def link_files(list):
  pass


def main():
  try:
    parser = ArgumentParser()

    #add_arg_options(parser)

    options = parser.parse_args()

    data = read_config('config.yaml')

    for k, v in data.items():
      if(k == 'backup'):
        backup_files(v)
      elif (k == 'install'):
        install_files(v)
      elif (k == 'link'):
        link_files(v)
      else:
        pass

  except OSError:
    print("FIALED SPLATESDSDEHLKJA:HFU*IH")


main()
