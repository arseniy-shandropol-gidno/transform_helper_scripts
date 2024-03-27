"""
Reads XML config from stdin to identify duplicate <ext:column name="..."/> names.
Outputs unique or duplicate status. Works with plain text, interactively via terminal,
ensuring input contains appropriate XML column tags.
"""

import re
import sys


def check_for_duplicate_column_names():
    print("Please paste your config text. Press Ctrl+D (Unix/Linux/Mac) or Ctrl+Z then Enter (Windows) when done.")

    # Read the entire input from stdin until EOF
    content = sys.stdin.read()

    # Regular expression to match <ext:column name="..."/>
    pattern = re.compile(r'<ext:column name="([^"]+)"')

    # Set to store column names
    column_names = set()

    # List to keep track of duplicates
    duplicates = []

    # Search for column names in the input content
    matches = pattern.findall(content)
    for name in matches:
        # Check if name already exists in the set
        if name in column_names:
            duplicates.append(name)
        else:
            column_names.add(name)

    # Check for duplicates
    if duplicates:
        print("Duplicate column names found:")
        for dup in set(duplicates):  # Print each duplicate only once
            print(dup)
    else:
        print("All column names are unique.")


# Run the function to check for duplicate column names
check_for_duplicate_column_names()
