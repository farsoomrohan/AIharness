import pandas as pd
import json

csv_file_path = 'hate_data.csv'
json_file_path = 'date_texts.json'  

df = pd.read_csv(csv_file_path)

texts_to_save = df['text'].iloc[:200].tolist()

json_data = [{'generated_text': text} for text in texts_to_save]

with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, indent=4)

print("complete")