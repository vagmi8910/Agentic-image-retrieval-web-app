import pickle
import os

def save_embeddings(embeddings, file_path):
    """
    Saves embeddings dictionary to a pickle file.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        pickle.dump(embeddings, f)
    print(f"Embeddings saved to {file_path}")

def load_embeddings(file_path):
    """
    Loads embeddings dictionary from a pickle file.
    Returns empty dict if file doesn't exist.
    """
    if not os.path.exists(file_path):
        return {}
    
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except (EOFError, pickle.UnpicklingError):
        # Return empty dict if file is empty or corrupted
        return {}
