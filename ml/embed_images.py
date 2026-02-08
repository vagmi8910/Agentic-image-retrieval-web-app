import os
import torch
from PIL import Image
from tqdm import tqdm
from .clip_model import CLIPModel

def embed_images(image_dir):
    """
    Computes embeddings for all images in a directory.
    Returns a dictionary {filename: embedding_tensor}.
    """
    clip_instance = CLIPModel()
    model = clip_instance.get_model()
    preprocess = clip_instance.get_preprocess()
    device = clip_instance.get_device()
    
    embeddings = {}
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(valid_extensions)]
    
    print(f"Found {len(image_files)} images to embed.")
    
    with torch.no_grad():
        for filename in tqdm(image_files, desc="Embedding Images"):
            image_path = os.path.join(image_dir, filename)
            try:
                image = Image.open(image_path).convert("RGB")
                image_input = preprocess(image).unsqueeze(0).to(device)
                image_features = model.encode_image(image_input)
                image_features /= image_features.norm(dim=-1, keepdim=True)
                embeddings[filename] = image_features.cpu()
            except Exception as e:
                print(f"Error embedding {filename}: {e}")
                
    return embeddings
