import os, shutil, subprocess, sys
import log
from log import LogLevel as ll

class SSH(object):
  """docstring for SSH"""
  def __init__(self, log):
    super(SSH, self).__init__()
    self.log = log

  def create_key(self, name, size, comment):
    l = self.log

    l.print("Creating a new key", ll.Debug)

    try:
      args = ['ssh-keygen',
              '-C', comment, 
              '-t', 'rsa', 
              '-b', size, 
              '-f', os.path.expanduser("~/.ssh/id_" + name),
              '-q',
              '-N', '']
      subprocess.run(args, check = True)
    except Exception as e:
      l.print("An error occurred creating a new key \n {}".format(e), ll.Error)
    else:
      l.print("Done", ll.Debug)

  def add_key_to_config(self, name, host, user, ident, port = 22):
    str = """Host {}
    HostName {}
    Port {}
    User {}
    IdentityFile {}
    IdentitiesOnly yes
          """.format(name, host, port, user, ident)
    with open(os.path.expanduser("~/.ssh/config"), 'a+') as f:
      f.write("\n" + str)
