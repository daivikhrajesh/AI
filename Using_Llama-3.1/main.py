import pandas as pd
import transformers
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login

# Authenticate with Hugging Face
login(token="Your HuggingFace Token")

# Disable memory efficient and flash attention
torch.backends.cuda.enable_mem_efficient_sdp(False)
torch.backends.cuda.enable_flash_sdp(False)

# Reading in the data file
df = pd.read_csv("universal_top_spotify_songs.csv")

# Subsetting dataset
df_in = df[df['country'] == 'IN'].reset_index(drop=True)

# Transform each row into a sentence
df_in['text'] = df_in.apply(lambda row: f"""
    Name: {row['name']}, 
    artists: {row['artists']}, 
    daily_rank: {row['daily_rank']},
    daily_movement: {row['daily_movement']},
    weekly_movement: {row['weekly_movement']},
    country: {row['country']},
    snapshot_date: {row['snapshot_date']},
    popularity: {row['popularity']},
    is_explicit: {row['is_explicit']},
    duration_ms: {row['duration_ms']},
    album_name: {row['album_name']},
    album_release_date: {row['album_release_date']},
    danceability: {row['danceability']},
    energy: {row['energy']},
    key: {row['key']},
    loudness: {row['loudness']},
    mode: {row['mode']},
    speechiness: {row['speechiness']},
    acousticness: {row['acousticness']},
    instrumentalness: {row['instrumentalness']},
    liveness: {row['liveness']},
    valence: {row['valence']},
    tempo: {row['tempo']},
    time_signature: {row['time_signature']}.""", axis=1)

# Stripping excess spaces
df_in['text'] = df_in['text'].str.strip()

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

# Add a padding token if it doesn't exist
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Tokenize the text
tokens = tokenizer(df_in['text'].tolist(), padding=True, truncation=True, max_length=50, return_tensors='pt')

# Initialize the text generation pipeline
model_id = "meta-llama/Llama-2-7b-hf"
pipeline = transformers.pipeline(
    "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
)

# Define the function to generate text
def get_completion_llama(prompt, model_pipeline=pipeline):
    response = model_pipeline(prompt, max_new_tokens=2000)
    return response[0]["generated_text"]

# Questions to ask the model
questions = [
    "What was the most famous song in India recently?",
    "What are some of the best acoustic songs?",
    "Are there any explicit songs? If yes please list them",
    "Name some famous artists who featured regularly on this list?"
]

# Generate responses for each question
for question in questions:
    prompt = f"""
    Using the following context information below please answer the following question
    to the best of your ability
    Context:
    {df_in['text'].tolist()}
    Question:
    {question}
    Answer:
    """
    answer = get_completion_llama(prompt)
    print(f"Question: {question}\nAnswer: {answer}\n")
