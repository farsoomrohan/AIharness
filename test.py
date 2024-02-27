from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch
import json

# load model
tokenizer = AutoTokenizer.from_pretrained("facebook/roberta-hate-speech-dynabench-r4-target")
model = AutoModelForSequenceClassification.from_pretrained("facebook/roberta-hate-speech-dynabench-r4-target")

# load texts from desired json file
with open('positive_data.json', 'r') as file:
    data = json.load(file)
texts = [item['generated_text'] for item in data]

# predict using model
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits
probabilities = softmax(logits, dim=1)
hate_speech_probabilities = probabilities[:, 1]

# print probability
for text, probability in zip(texts, hate_speech_probabilities):
    print(f"Text: {text}")
    print(f"Hate Speech Probability: {probability.item()}")