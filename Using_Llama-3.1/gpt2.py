from transformers import GPT2Tokenizer, GPT2Model
import pandas as pd

# Load the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2Model.from_pretrained("gpt2")

# Set the padding token to the end-of-sequence token
tokenizer.pad_token = tokenizer.eos_token

# Example DataFrame
df_in = pd.DataFrame({
    'text': ["Hello, how are you?", "I'm doing fine, thank you!"]
})

# Tokenize the text
tokens = tokenizer(df_in['text'].tolist(), padding=True, truncation=True, max_length=50, return_tensors='pt')

print(tokens)
