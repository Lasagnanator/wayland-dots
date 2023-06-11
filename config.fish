##### TITLE #####
function fish_title
    echo "Terminal"
end

##### LOGIN SHELL PARAMETERS #####
set fish_greeting "Sphinx of black quartz, judge my vow ~"
set -gx GTK_THEME 'Tokyonight-Storm-BL'
set -gx QT_QPA_PLATFORMTHEME 'gtk2'

##### INTERACTIVE SHELL PARAMETERS #####
if status is-interactive

    ##### EXPORT #####
    set -gx EDITOR 'nvim'
    set -gx VISUAL 'nvim' 
    set -gx PATH $PATH ~/.local/bin ~/.scripts ~/.scripts/monitors

    ##### ALIAS #####
    # System
    alias pac 'sudo pacman'
    alias grep 'grep --color'
    alias diff 'diff --color=auto'
    alias ip 'ip -color=auto'
    # Programs
    alias v 'nvim'
    alias vi 'nvim'
    alias vim 'nvim'
    alias sv 'sudo -E nvim'
    alias g 'git'
    alias xp '. ranger'
    alias lz 'lazygit'
    alias bt 'bluetoothctl'
    alias prsync 'rsync -r --info=progress2'
    alias itop 'sudo intel_gpu_top'
    alias dbeaver-cmp '/home/lasagnanator/Git/dbeaver/product/community/target/products/org.jkiss.dbeaver.core.product/linux/gtk/x86_64/dbeaver/dbeaver'
    # Python
    alias vFlask 'source /home/lasagnanator/VENV/vFlask/bin/activate'
    alias flaskHosting 'source /home/lasagnanator/VENV/flaskHosting/bin/activate'
    alias mHealth 'source /home/lasagnanator/VENV/mHealth/bin/activate'
    alias vJupyter 'source /home/lasagnanator/VENV/vJupyter/bin/activate'
    # CD to some shit
    alias ssh-homeserver 'source ssh-homeserver'
    alias mount-homeserver 'source mount-homeserver'
    alias unmount-homeserver 'source unmount-homeserver'
    # Vagrant
    alias vagrant-ssh 'TERM=xterm-256color vagrant ssh'

    ##### ABBREVIATION #####
    abbr -a USB /run/media/lasagnanator 

    ##### KEYBINDS #####
    if [ $TERM = 'xterm-256color' ]
        bind \b backward-kill-word
        bind \e\[3\;5~ kill-word
    end

    ##### FZF #####
    set fzf_fd_opts --hidden --exclude=.git --no-ignore
    fzf_configure_bindings --variable=\e\cv --directory=\cq

    ##### STARSHIP #####
    starship init fish | source
end
