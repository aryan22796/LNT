# In this example, we will use ChainMap to manage configurations from different sources, 
# such as default settings, user settings, and command-line arguments.
from collections import ChainMap

# Default settings
defaults = {'theme': 'dark', 'show_line_numbers': True, 'tab_size': 4}

# User settings (overrides defaults)
user_settings = {'theme': 'light', 'tab_size': 2}

# Command-line arguments (overrides both defaults and user settings)
cli_args = {'show_line_numbers': False}

# Creating a ChainMap
settings = ChainMap(cli_args, user_settings, defaults)

print(settings['theme'])            # Output: 'light' (from user_settings)
print(settings['show_line_numbers'])  # Output: False (from cli_args)
print(settings['tab_size'])         # Output: 2 (from user_settings)
