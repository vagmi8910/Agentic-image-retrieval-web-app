import torch

def find_similar_images(query_embedding, image_embeddings, top_k=5):
    """
    Finds the most similar images to the query embedding.
    
    Args:
        query_embedding (torch.Tensor): Tensor of shape (1, embedding_dim)
        image_embeddings (dict): Dictionary {filename: embedding_tensor}
        top_k (int): Number of top results to return.
        
    Returns:
        List of tuples (filename, score) sorted by score descending.
    """
    results = []
    
    for filename, img_emb in image_embeddings.items():
        # Ensure img_emb is shape (1, dim), if it's just (dim), unsqueeze it
        if img_emb.dim() == 1:
            img_emb = img_emb.unsqueeze(0)
            
        # Cosine similarity
        similarity = torch.nn.functional.cosine_similarity(query_embedding, img_emb)
        results.append((filename, similarity.item()))
        
    # Sort by score descending
    results.sort(key=lambda x: x[1], reverse=True)
    
    return results[:top_k]
