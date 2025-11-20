from transformers import AutoTokenizer
from transformers import pipeline

# Tokenization
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Transformers are amazing"
tokens = tokenizer.tokenize(text)
print(tokens)

inputs = tokenizer(text, return_tensors="pt")
print(inputs)

# Pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
context = """
The Nile River is the longest river in the world. It flows through Egpyt and Sudan. 
"""
question = "Which river is the longest in the world?"
result = qa_pipeline(question=question, context=context)
print(result)