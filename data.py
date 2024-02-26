from transformers import pipeline
import json

generator = pipeline('text-generation', model='gpt2')

prompt = "Share a positive thought about today."

generatedtexts = []

for _ in range(200):
    response = generator(prompt, max_length=50, num_return_sequences=1, temperature=0.7)
    generated_text = response[0]['generated_text'].strip()
    sentence = generated_text[len(prompt):].split('.')[0] + '.'
    generatedtexts.append({"generated_text": sentence.strip()})

with open('positive_sentences.json', 'w') as file:
    json.dump(generatedtexts, file, indent=4)

print("complete")
