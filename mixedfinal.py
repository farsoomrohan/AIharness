import pandas as pd
import json


csv_file_path = 'hate_data.csv'
df = pd.read_csv(csv_file_path)

extracted_texts = df.loc[249:349, 'text'] 

new_data = [{"generated_text": text, "score": 1} for text in extracted_texts]

json_file_path = 'mixed_lines.json'

with open(json_file_path, 'r') as file:
    existing_data = json.load(file)

updated_data = existing_data + new_data

with open(json_file_path, 'w') as file:
    json.dump(updated_data, file, indent=4)
