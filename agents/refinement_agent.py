class RefinementAgent:
    def __init__(self):
        pass

    def refine_query(self, query):
        """
        Enhances the query for better retrieval performance.
        """
        query = query.strip()
        
        # Add "a photo of" if not present
        if not query.lower().startswith(("a photo of", "an image of", "picture of")):
             return f"a photo of {query}"
        
        return query
