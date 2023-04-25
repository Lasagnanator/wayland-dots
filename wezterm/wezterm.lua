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
-- Possible colorschemes: AdventureTime, Andromeda, tokyonight_variant, Tokyo Night [Variant] (Gogh)

config.window_background_opacity = 0.85

config.hide_tab_bar_if_only_one_tab = true

config.font = wezterm.font ( 'Iosevka Term', { weight = 'DemiBold' } )
config.font_size = 11.0
config.cell_width = 0.8

config.keys = {
  {
    key = ' ',
    mods = 'SHIFT',
    action = wezterm.action.SendKey {
            key = ' '
        },
  },
}

-- And finally, return the configuration to wezterm
return config
