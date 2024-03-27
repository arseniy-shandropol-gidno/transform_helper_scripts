"""
This script reads XML configuration data from stdin to identify duplicates based on <ext:column> tags.
It prioritizes the 'alias' attribute value over the 'name' attribute for comparison. If an 'alias' exists,
it is compared; otherwise, the 'name' attribute is used. This approach ensures unique identification of
columns, preferring 'alias' values when available.

The script outputs the status of the column attributes (name or alias), indicating whether they are unique
or duplicates. It works with plain text input, interactively via the terminal, and requires the input to contain
appropriate XML <ext:column> tags with 'name' and optionally 'alias' attributes.

Usage:
- Run the script.
- Paste your XML config text into the terminal.
- Signal end of input by pressing Ctrl+D (Unix/Linux/Mac) or Ctrl+Z then Enter (Windows).
- Review the script's output to identify any duplicate column attributes based on the criteria mentioned.
"""

import re
import sys

def check_for_duplicate_column_attributes():
    print("Please paste your config text. Press Ctrl+D (Unix/Linux/Mac) or Ctrl+Z then Enter (Windows) when done.")

    # Read the entire input from stdin until EOF
    content = sys.stdin.read()

    # Regular expression to match <ext:column name="..." alias="..."/> if alias exists
    # This pattern captures both 'name' and 'alias' attributes if they exist
    pattern = re.compile(r'<ext:column name="([^"]+)"(?:.*?alias="([^"]+)")?')

    # Set to store column attributes (name or alias)
    column_attributes = set()

    # List to keep track of duplicates
    duplicates = []

    # Search for column names and aliases in the input content
    matches = pattern.findall(content)
    for name, alias in matches:
        # Prefer alias if it exists, otherwise use name
        attribute = alias if alias else name

        # Check if attribute already exists in the set
        if attribute in column_attributes:
            duplicates.append(attribute)
        else:
            column_attributes.add(attribute)

    # Check for duplicates
    if duplicates:
        print("Duplicate column attributes found:")
        for dup in set(duplicates):  # Print each duplicate only once
            print(dup)
    else:
        print("All column attributes are unique.")

# Run the function to check for duplicate column attributes
check_for_duplicate_column_attributes()
