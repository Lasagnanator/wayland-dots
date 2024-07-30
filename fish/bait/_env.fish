##### ENVIRONMENTAL VARIABLES #####

set fish_greeting "Sphinx of black quartz, judge my vow ~"
set -gx GTK_THEME 'Tokyonight-Storm-BL'
set -gx QT_QPA_PLATFORMTHEME 'gtk2'
set -gx EDITOR 'nvim'
set -gx VISUAL 'nvim' 
set -gx PATH $PATH ~/.local/bin ~/.scripts

function get-kubeconfig
    set -l KUBE_FILES ''
    for FILE in $(find "$HOME/.kube/conf.d" -type f)
        set KUBE_FILES "$KUBE_FILES$FILE:"
    end
    echo $(string trim --right --chars=':' $KUBE_FILES)
end
set -gx KUBECONFIG $(get-kubeconfig)
