import re
import sys

def transform_config_from_input():
    print("Please paste your config text. Press Ctrl+D (Unix/Linux/Mac) or Ctrl+Z then Enter (Windows) when done.")

    # Read from stdin until EOF
    content = sys.stdin.read()

    # Adjusted regular expression to match <column name="..." alias="..."/> (capture both name and optionally alias)
    pattern = re.compile(r'<column name="([^"]+)"(?:\s+alias="([^"]+)")?')

    # Find all matches
    matches = pattern.findall(content)

    # Generate and print the transformed <ext:column name="..."/> tags
    for match in matches:
        name, alias = match
        effective_name = alias if alias else name
        print(f'<ext:column name="{effective_name}"/>')

# Process input and transform
transform_config_from_input()
