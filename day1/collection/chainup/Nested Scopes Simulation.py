# we simulate nested variable scopes using ChainMap. 
# We will define a function that modifies and accesses variables within nested scopes.
from collections import ChainMap

def nested_scopes_example():
    global_scope = {'x': 1, 'y': 2}
    local_scope = {'y': 3, 'z': 4}
    
    # Create the ChainMap for scopes
    scope = ChainMap(local_scope, global_scope)
    
    print(f"Initial x: {scope['x']}")  # Output: 1
    print(f"Initial y: {scope['y']}")  # Output: 3
    
    # Modify the local scope
    scope['x'] = 10
    scope['y'] = 20
    
    print(f"Modified x: {scope['x']}")  # Output: 10
    print(f"Modified y: {scope['y']}")  # Output: 20
    
    # Access global scope
    print(f"Global x: {global_scope['x']}")  # Output: 1
    print(f"Local y: {local_scope['y']}")    # Output: 20

nested_scopes_example()



# ChainMap is a powerful tool for managing multiple dictionaries in a unified manner.
#    It is useful for combining configurations, simulating nested scopes, and more. By understanding its basic usage 
# and capabilities, you can effectively leverage ChainMap in various advanced scenarios.