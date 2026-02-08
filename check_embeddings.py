import pickle
import torch
import os

EMBEDDINGS_PATH = "embeddings/image_embeddings.pkl"

if not os.path.exists(EMBEDDINGS_PATH):
    print("No embeddings file found.")
    exit(0)

try:
    with open(EMBEDDINGS_PATH, 'rb') as f:
        data = pickle.load(f)

    if not data:
        print("Embeddings file is empty.")
    else:
        first_key = list(data.keys())[0]
        first_emb = data[first_key]
        print(f"Found {len(data)} embeddings.")
        print(f"Embedding shape: {first_emb.shape}")
        
        if first_emb.shape[-1] == 512:
             print("DETECTED: Old 512-dim embeddings (ViT-B-32).")
        elif first_emb.shape[-1] == 768:
             print("DETECTED: New 768-dim embeddings (ViT-L-14).")
        else:
             print(f"Unknown dimension: {first_emb.shape[-1]}")

except Exception as e:
    print(f"Error reading embeddings: {e}")
