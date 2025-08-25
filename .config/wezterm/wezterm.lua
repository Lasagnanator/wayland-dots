local wezterm = require 'wezterm'

-- This table will hold the configuration.
local config = {}

-- In newer versions of wezterm, use the config_builder which will
-- help provide clearer error messages
if wezterm.config_builder then
  config = wezterm.config_builder()
end

-- This is where you actually apply your config choices

-- For example, changing the color scheme:
config.color_scheme = 'tokyonight_night'
-- Possible colorschemes: AdventureTime, Andromeda, tokyonight_variant, Tokyo Night [Variant] (Gogh), SynthwaveAlpha
-- config.default_prog = { 'bash' } -- remove for other login shell
-- config.window_background_opacity = 0.85
config.hide_tab_bar_if_only_one_tab = true
config.window_padding = {
  left = 4,
  right = 4,
  top = 4,
  bottom = 4,
}
config.font = wezterm.font_with_fallback { { family = 'JetBrains Mono',  weight = 'Regular' }, { family = 'Symbols Nerd Font',  weight = 'Regular' } }
config.font_size = 11.0
-- config.cell_width = 0.8

config.keys = {
    {
        key = ' ',
        mods = 'SHIFT',
        action = wezterm.action.SendKey {
            key = ' '
        },
    },
    {
        key = 'Enter',
        mods = 'SUPER|CTRL',
        action = wezterm.action.SpawnWindow,
    },
    {
        key = ';',
        mods = 'CTRL',
        action = wezterm.action.SendKey {
            key = 'Escape'
        },
    },
}

-- wezterm.on('format-window-title', function ()
--     return 'Terminal'
-- end)

-- And finally, return the configuration to wezterm
return config
