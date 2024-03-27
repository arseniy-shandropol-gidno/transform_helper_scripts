"""
Converts XML config input from stdin into a JSON representation of a field set,
utilizing <ext:column name="..." alias="..."/> tags for field names.
Input: plain text XML. Output: JSON structure with field set details.
Operates interactively in a terminal, focusing on name and alias attributes for conversion.
"""

import json
import re
import sys

def snake_case_to_camel_case(name):
    parts = name.split('_')
    return parts[0] + ''.join(part.capitalize() for part in parts[1:])

def generate_json():
    # Static JSON template
    json_template = {
        "legend": "members table",
        "collapsible": False,
        "key": "fieldsetLatest",
        "type": "fieldsetLatest",
        "label": "Field Set",
        "input": False,
        "customClass": "bootstrapFormStyles mdtuddm-fieldset",
        "tableView": False,
        "components": [],
        "id": "eqnfez"
    }

    print("Please paste your config text. Press Ctrl+D (Unix/Linux/Mac) or Ctrl+Z then Enter (Windows) when done.")
    content = sys.stdin.read()

    # Adjusted regular expression to match <ext:column name="..." alias="..."/> (if alias is present)
    pattern = re.compile(r'<ext:column name="([^"]+)"(?:\s+alias="([^"]+)")?')
    matches = pattern.findall(content)

    # Generate components
    components = []
    for match in matches:
        name, alias = match
        effective_name = alias if alias else name
        components.append({
            "label": effective_name,
            "autocomplete": "on",
            "mask": False,
            "trimSpaces": False,
            "key": snake_case_to_camel_case(effective_name),
            "tableView": True,
            "customColumnWidth": False,
            "sortAsNumber": False,
            "type": "textfieldLatest",
            "input": True,
            "customClass": "mdtuddm-textfield",
            "inputType": "text",
            "inputFormat": "plain",
            "spellcheck": True,
            "truncateMultipleSpaces": False
        })

    # Insert components into the template
    json_template["components"] = components

    # Output the final JSON
    print(json.dumps(json_template, indent=4))

# Execute the function
if __name__ == "__main__":
    generate_json()
