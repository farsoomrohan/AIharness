import csv
import json

csv_file_path = 'FinalBalancedDataset.csv'
json_file_path = 'tweets_with_scores.json'

data = []

with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        
        data.append({
            "generated_text": row['tweet'],
            "score": int(row['Toxicity'])  
        })

with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)

print(f"Data has been successfully converted and saved to {json_file_path}")
