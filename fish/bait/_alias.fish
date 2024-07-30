##### GENERAL ALIASES #####

# Colors
alias grep 'grep --color'
alias diff 'diff --color=auto'
alias ip 'ip -color=auto'

# Utilities
alias v 'nvim'
alias vi 'nvim'
alias vim 'nvim'
alias sv 'sudo -E nvim'
alias g 'git'
alias r 'ranger-cd'
alias d 'docker'
alias k 'kubectl'
alias t 'task'
alias tf 'terraform'
alias lz 'lazygit'
alias ldk 'lazydocker'
alias bt 'bluetoothctl'
alias fman "man -k . | awk '{print \$1}' | fzf --header 'Select a command to open in man' --preview 'man {}' | xargs man"
alias kdesc "kubectl get pods -A --no-headers | fzf | awk '{print \$2, \$1}' | xargs -n 2 sh -c 'kubectl describe pod \$0 -n \$1' | less --mouse"

# Packet managers
alias pac 'sudo pacman'
alias zyp 'sudo zypper'
alias dnf 'sudo dnf'
alias apt 'sudo apt'
