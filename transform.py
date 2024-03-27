"""
This script transforms XML column configurations by reading from stdin, targeting <column> tags.
It extracts 'name' attributes from these tags and outputs each as an <ext:column> tag with
the original 'name' value preserved. Designed for interactive terminal use, users paste their configuration,
signal EOF, and receive transformed tags instantly.

Usage:
- Run the script in a terminal.
- Paste the XML configuration text.
- Complete input with Ctrl+D (Unix/Linux/Mac) or Ctrl+Z then Enter (Windows).
- The script outputs transformed <ext:column> tags for each original <column> tag.
"""


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

