import json

text_file_path = 'mixed.txt'

mixed_lines_data = []

with open(text_file_path, 'r') as file:
    for line in file:
        clean_line = line.strip()
        if clean_line:
            line_data = {"generated_text": clean_line, "score": 0}
            mixed_lines_data.append(line_data)

json_file_path = 'mixed_lines.json'

with open(json_file_path, 'w') as file:
    json.dump(mixed_lines_data, file, indent=4)