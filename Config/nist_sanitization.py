import os

file_path = 'NIST_File/nist.json'

# FIXME: Implement a better sanitizer, this is ugly af f... geez
with open(file_path) as file:
    for data in file:
        json_path = 'NIST_File/nist_sanitized.json'
        json_mode = 'a' if os.path.exists(json_path) else 'w'
        with open(json_path, json_mode) as json_data:
            string_to_bool = data.replace('"✓"', 'true')
            string_to_bool = string_to_bool.replace('"level1": ""', '"level1": false')
            string_to_bool = string_to_bool.replace('"level2": ""', '"level2": false')
            string_to_bool = string_to_bool.replace('"level3": ""', '"level3": false')

            json_data.write(string_to_bool)
        