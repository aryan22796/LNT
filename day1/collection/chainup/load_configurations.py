from collections import ChainMap

def load_config(override_dict=None):
    import config_default
    import config_override
    
    # Create the ChainMap
    config = ChainMap(override_dict or {}, config_override.override_config, config_default.default_config)
    
    return config

# Example usage
custom_override = {'debug': True, 'host': '192.168.1.1'}
config = load_config(custom_override)

print(config['host'])  # Output: '192.168.1.1'
print(config['port'])  # Output: 9090
print(config['debug'])  # Output: True
