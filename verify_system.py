import torch
from agents.planner_agent import PlannerAgent
from ml.embed_text import embed_text

def test_system():
    print("Initializing test...")
    
    # 1. Create Dummy Embeddings (Dimensions must match CLIP ViT-B-32: 512)
    embedding_dim = 512
    dummy_embeddings = {
        "image1.jpg": torch.randn(1, embedding_dim),
        "image2.jpg": torch.randn(1, embedding_dim),
        "image3.jpg": torch.randn(1, embedding_dim)
    }
    
    # Normalize them to simulate real embeddings
    for k, v in dummy_embeddings.items():
        dummy_embeddings[k] = v / v.norm(dim=-1, keepdim=True)
        
    print(f"Created {len(dummy_embeddings)} dummy embeddings.")
    
    # 2. Initialize Planner Agent
    try:
        planner = PlannerAgent()
        print("Planner Agent initialized.")
    except Exception as e:
        print(f"Failed to initialize Planner Agent: {e}")
        return

    # 3. Test Query
    query = "test query"
    print(f"Testing query: '{query}'")
    
    try:
        results, intent = planner.run(query, dummy_embeddings)
        print("Planner run successful.")
        print(f"Intent parsed: {intent}")
        print(f"Number of results: {len(results)}")
        
        if results:
            print(f"Top result: {results[0]}")
        else:
            print("No results returned (might be due to threshold filtering).")
            
    except Exception as e:
        print(f"Error during planner execution: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_system()
