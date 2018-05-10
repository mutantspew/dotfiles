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

  def run(self):
    l = self.log

    l.print("\n\nGit Config", ll.Info)
    
    # setup the git global config file
    if(self.config['create_config_file'] == True):
      # self.setup_git_config()
      print("TODO RE-ENABLE GIT CONFIG")

    # setup our hosts
    self.create_hosts(self.config['hosts'])
      

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

    with open(dest, 'w') as f:
      f.write(str)

    l.print("Done with git config", ll.Debug)

  def create_hosts(self, hosts):

    for host in hosts.items():
      key = host[1] # gets the key section

      create = key['key']['create']
      if(create == True):
        self.log.print("Create True", ll.Debug)
      else:
        self.log.print("Create False", ll.Debug)

      name = key['key']['name']
      self.log.print(name, ll.Debug)

      host = key['key']['host']
      self.log.print(host, ll.Debug)
      
      size = key['key']['size']
      self.log.print(size, ll.Debug)

      user = key['key']['user']
      self.log.print(user, ll.Debug)

      port = key['key']['port']
      self.log.print(port, ll.Debug)

      comment = key['key']['comment']
      self.log.print(comment, ll.Debug)

      if(create == True): # create our key
        self.log.print("Creating ssh key")
        self.ssh.create_key(name, size, comment)

      if(key['add_to_config'] == True):
        self.log.print("Adding to .ssh/config")
        self.ssh.add_key_to_config(name, host, user, "~/.ssh/id_" + name, port)
