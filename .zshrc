### ZINIT ###
# Bootstrap
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"
if [[ ! -d "$ZINIT_HOME" ]]; then
   mkdir -p "$(dirname "$ZINIT_HOME")"
   git clone 'https://github.com/zdharma-continuum/zinit.git' "$ZINIT_HOME"
fi
source "${ZINIT_HOME}/zinit.zsh"

# Plugins
zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light Aloxaf/fzf-tab

# Snippets
zinit snippet OMZP::command-not-found
zinit snippet OMZP::eza

### COMPLETION ###
autoload -Uz compinit && compinit
zinit cdreplay -q
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color $realpath'
zstyle ':fzf-tab:complete:__zoxide_z:*' fzf-preview 'ls --color $realpath'

### OPTIONS ###
setopt autocd
# setopt correct
unsetopt beep

### HISTORY ###
export HISTSIZE=5000
export HISTFILE="${HOME}/.histfile"
export SAVEHIST="${HISTSIZE}"
export HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups

### KEYBINDS ###
bindkey -e
bindkey '^[w' kill-region

### ENVS ###
export EDITOR='nvim'
export VISUAL='nvim' 
export PATH="$PATH:~/.local/bin:~/.scripts"
export COLORTERM='truecolor'

### ALIASES ###
# Colors
alias grep='grep --color'
alias diff='diff --color=auto'
alias ip='ip -color=auto'

# Utilities
alias v='nvim'
alias vi='nvim'
alias vim='nvim'
alias sv='sudo -E nvim'
alias g='git'
alias r='ranger-cd'
alias d='docker'
alias k='kubectl'
alias t='task'
alias tf='terraform'
alias lz='lazygit'
alias ldk='lazydocker'
alias bt='bluetoothctl'

# Packet managers
alias pac='sudo pacman'
alias zyp='sudo zypper'
alias dnf='sudo dnf'
alias apt='sudo apt'

### PER-ENVIRONMENT CONFIGURATION ###
if [[ ! -d "${HOME}/.zshrc.d" ]]; then
   mkdir -p "${HOME}/.zshrc.d"
fi
for rc in "${HOME}/.zshrc.d/"*(N); do
    if [[ -f "${rc}" ]]; then
        source "${rc}"
    fi
done
unset rc

### INTEGRATIONS ###
eval "$(fzf --zsh)"
eval "$(zoxide init zsh)"
eval "$(direnv hook zsh)"
eval "$(starship init zsh)"
# eval "$(oh-my-posh init zsh --config ~/.config/oh-my-posh/config.toml)"

### SDKMAN ###
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
