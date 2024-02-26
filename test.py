from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch


tokenizer = AutoTokenizer.from_pretrained("facebook/roberta-hate-speech-dynabench-r4-target")
model = AutoModelForSequenceClassification.from_pretrained("facebook/roberta-hate-speech-dynabench-r4-target")

texts = ["i hate you", "I love sunny days"]

inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

probabilities = softmax(logits, dim=1)

hate_speech_probabilities = probabilities[:, 1]
print(hate_speech_probabilities)

for text, probability in zip(texts, hate_speech_probabilities):
    print(f"Text: {text}")
    print(f"Hate Speech Probability: {probability.item()}")