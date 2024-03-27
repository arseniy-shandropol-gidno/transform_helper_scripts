import re
import sys


def transform_config_from_input():
    print("Please paste your config text. Press Ctrl+D (Unix/Linux/Mac) or Ctrl+Z then Enter (Windows) when done.")

    # Read from stdin until EOF
    content = sys.stdin.read()

    # Regular expression to match <column name="..."/>
    pattern = re.compile(r'<column name="([^"]+)"')

    # Find all matches
    column_names = pattern.findall(content)

    # Generate and print the transformed <ext:column name="..."/> tags
    for name in column_names:
        print(f'<ext:column name="{name}"/>')


# Process input and transform
transform_config_from_input()
