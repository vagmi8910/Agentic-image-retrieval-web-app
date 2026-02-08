import torch
from .clip_model import CLIPModel

def embed_text(text):
    """
    Computes embedding for a text query.
    Returns: torch.Tensor of shape (1, embedding_dim)
    """
    clip_instance = CLIPModel()
    model = clip_instance.get_model()
    tokenizer = clip_instance.get_tokenizer()
    device = clip_instance.get_device()
    
    with torch.no_grad():
        text_input = tokenizer([text]).to(device)
        text_features = model.encode_text(text_input)
        text_features /= text_features.norm(dim=-1, keepdim=True)
        
    return text_features.cpu()
