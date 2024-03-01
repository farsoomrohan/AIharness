from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch
import json

tokenizer = AutoTokenizer.from_pretrained("facebook/roberta-hate-speech-dynabench-r4-target")
model = AutoModelForSequenceClassification.from_pretrained("facebook/roberta-hate-speech-dynabench-r4-target")

with open('mixed_lines.json', 'r') as file:
    data = json.load(file)
texts = [item['generated_text'] for item in data]
original_scores = [item['score'] for item in data]

inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits
probabilities = softmax(logits, dim=1)
model_scores = probabilities[:, 1]

new_data = [
    {"generated_text": text, "original_score": original, "model_score": model_score.item()}
    for text, original, model_score in zip(texts, original_scores, model_scores)
]

with open('tested_mixed_data.json', 'w') as outfile:
    json.dump(new_data, outfile, indent=4)

for item in new_data:
    print(f"Text: {item['generated_text']}")
    print(f"Original Score: {item['original_score']}")
    print(f"Model Score: {item['model_score']}")
    print()