##### TITLE #####
function fish_title
    echo "Terminal"
end

##### ENVIRONMENT #####
source {$__fish_config_dir}/bait/_env.fish

if status is-interactive

    # Source extra configuration files
    source {$__fish_config_dir}/bait/_alias.fish
    source {$__fish_config_dir}/bait/_keybinds.fish
    source {$__fish_config_dir}/bait/_plugins.fish
    if test ! -e {$__fish_config_dir}/bait/additional.fish
        touch {$__fish_config_dir}/bait/additional.fish
    end
    source {$__fish_config_dir}/bait/additional.fish

    # Starship prompt
    starship init fish | source
end
