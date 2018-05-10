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
      l = self.log
      key = host[1] # gets the key section


      temp = self.check_key(key['key'], 'create')
      create = temp if temp is not None else True
      
      name = self.check_key(key['key'], 'name')

      if name is None:
        l.print("Name is None", ll.Error)
        sys.exit()

      host = self.check_key(key['key'], 'host')

      if host is None:
        l.print("Host is None", ll.Error)
        sys.exit()

      temp = self.check_key(key['key'], 'size')
      size = temp if temp is not None else "2048"
      
      user = self.check_key(key['key'], 'user')

      if user is None:
        l.print("User is None", ll.Error)
        sys.exit()

      temp = self.check_key(key['key'], 'port')
      port = temp if temp is not None else "22"

      temp = self.check_key(key['key'], 'comment')
      comment = temp if temp is not None else ''


      if(create == True):
        l.print("Create True", ll.Debug)
      else:
        l.print("Create False", ll.Debug)

      path = "~/.ssh/id_{}".format(name)

      if(create == True): # create our key
        l.print("Creating ssh key")
        self.ssh.create_key(path, size, comment)

      if(key['add_to_config'] == True):
        l.print("Adding to .ssh/config")
        self.ssh.add_key_to_config(name, host, user, path, port)
  
  # checks if key is in dictionary, if it is returns the value otherwise none
  def check_key(self, dict, key):
    self.log.print("Checking for {}".format(key), ll.Debug)

    if(key in dict):
      self.log.print('Found!', ll.Debug)
      return dict[key]
    else:
      self.log.print("Key {} Not Found!".format(key), ll.Warn)
      return None
