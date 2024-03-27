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

    # Adjusted regular expression to match <ext:column name="..."/>
    pattern = re.compile(r'<ext:column name="([^"]+)"')
    column_names = pattern.findall(content)

    # Generate components
    components = []
    for name in column_names:
        components.append({
            "label": name,
            "autocomplete": "on",
            "mask": False,
            "trimSpaces": False,
            "key": snake_case_to_camel_case(name),
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
