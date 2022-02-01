import yaml
# YAML is a human-readable data-serialization language.
# It uses both Python-style indentation to indicate nesting, 
# and a more compact format that uses [...] for lists and {...} for maps
# thus JSON files are valid YAML

__config = None

# Este código se usa para evitar varias llamadas a disco al
# querer leer el archivo YAML

def config():
    global __config
    if not __config:
        with open('config.yaml') as f:
            # yaml.load() is deprecated
            __config = yaml.safe_load(f)
            # safe_load() returns a dict.
    return __config

# Aquí estamos aplicando el POM (Page Object Model)