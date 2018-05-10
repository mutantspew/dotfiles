import os, sys
import ssh
import log
from log import LogLevel as ll

class Git(object):
  """docstring for Git"""
  def __init__(self, log, gitconfig):
    super(Git, self).__init__()
    self.log = log
    self.ssh = ssh.SSH(log)
    self.config = gitconfig

  def key(self):
    pass

  def run(self):
    l = self.log

    l.print("\n\nGit Config", ll.Info)
    
    self.setup_git_config()

    l.print("\n\n")

  def setup_git_config(self):
    l = self.log

    l.print("Setting up git config", ll.Debug)
    print('\n')
    name = input('Enter name: ')
    email = input('Enter email: ')

    str = """[color]
  ui = true
[user]
  name = {}
  email = {}
""".format(name, email)

    dest = os.path.abspath('config/git/.gitconfig')

    print(dest)

    with open(dest, 'w') as f:
      f.write(str)

    l.print("Done with git config", ll.Debug)
