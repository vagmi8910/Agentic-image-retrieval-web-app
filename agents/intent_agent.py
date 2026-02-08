import re

class IntentAgent:
    def __init__(self):
        pass

    def extract_intent(self, query):
        """
        Analyzes the user query to determine intent and extract keywords.
        """
        query = query.strip()
        
        # Basic keyword extraction (remove common stopwords)
        stopwords = {'a', 'an', 'the', 'in', 'on', 'at', 'of', 'for', 'with', 'by'}
        words = re.findall(r'\b\w+\b', query.lower())
        keywords = [w for w in words if w not in stopwords]
        
        intent = {
            "type": "search",  # Default to search
            "original_query": query,
            "keywords": keywords,
            "is_vague": len(keywords) < 2 
        }
        
        return intent
