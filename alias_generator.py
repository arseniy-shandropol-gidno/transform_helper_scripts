"""
Processes XML input from stdin, identifying common column names across tables,
appending table aliases to avoid conflicts. Input: plain text XML with <table> and <ext:column> tags.
Output: modified XML with unique column aliases for shared column names.
Interactive terminal input required.
"""

def process_tables(tables):
    # Identify common column names
    column_names = {}
    for table in tables:
        start = table.find('alias="') + 7
        end = table.find('"', start)
        table_alias = table[start:end]
        columns_start = table.find('>') + 1
        columns_end = table.rfind('<')
        columns_section = table[columns_start:columns_end]
        columns = columns_section.split('<ext:column')
        for column in columns:
            if 'name="' in column:
                name_start = column.find('name="') + 6
                name_end = column.find('"', name_start)
                column_name = column[name_start:name_end]
                if column_name not in column_names:
                    column_names[column_name] = [table_alias]
                else:
                    column_names[column_name].append(table_alias)

    # Append aliases to common column names
    for table in tables:
        start = table.find('alias="') + 7
        end = table.find('"', start)
        table_alias = table[start:end]
        for column_name, aliases in column_names.items():
            if len(aliases) > 1 and table_alias in aliases:
                old = f'<ext:column name="{column_name}"'
                new = f'<ext:column name="{column_name}" alias="{column_name}_{table_alias}"'
                table = table.replace(old, new)
        print(table)
        print()  # Separate tables for clarity

def main():
    tables = []
    while True:
        input_lines = []
        line = input()
        if line == "DONE":
            break
        while line:
            input_lines.append(line)
            line = input()
        tables.append("\n".join(input_lines))

    process_tables(tables)

if __name__ == "__main__":
    main()
