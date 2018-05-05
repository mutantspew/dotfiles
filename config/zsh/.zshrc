# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
  export ZSH=/home/jacob/.oh-my-zsh
  export ZSH_CUSTOM

# Set name of the theme to load. 
ZSH_THEME="candy"

# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
DISABLE_UNTRACKED_FILES_DIRTY="true"

# plugins to load
plugins=(
          bundler
          colored-man-pages
          gem
          git
          heroku
          node
          npm
          nvm
          postgres
          python
          rails
          rake
          ruby
          rvm
          ssh-agent
          sublime
          systemd
          tmux
          ubuntu
          zsh-autosuggestions
          zsh_reload
        )

source $ZSH/oh-my-zsh.sh

# configuration files for zsh

source "$HOME/.zsh-scripts/.aliases.sh"
source "$HOME/.zsh-scripts/.exports.sh"
source "$HOME/.zsh-scripts/.functions.sh"

source "$HOME/.zsh-scripts/.ssh.sh"

# Add RVM to PATH for scripting. Make sure this is the last PATH variable change.
export PATH="$PATH:$HOME/.rvm/bin"
[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"  # This loads RVM into a shell session