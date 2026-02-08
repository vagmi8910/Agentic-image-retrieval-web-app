import torch
import open_clip

class CLIPModel:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CLIPModel, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        print("Loading CLIP model...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, _, self.preprocess = open_clip.create_model_and_transforms('ViT-L-14', pretrained='laion2b_s32b_b82k')
        self.model.to(self.device)
        self.model.eval()
        self.tokenizer = open_clip.get_tokenizer('ViT-L-14')
        print(f"Model loaded on {self.device}")

    def get_model(self):
        return self.model
    
    def get_preprocess(self):
        return self.preprocess
    
    def get_tokenizer(self):
        return self.tokenizer
    
    def get_device(self):
        return self.device
