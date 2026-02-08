class EvaluatorAgent:
    def __init__(self, threshold=0.15):
        self.threshold = threshold

    def evaluate_results(self, results):
        """
        Filters and ranks search results.
        
        Args:
            results (list): List of tuples (filename, score)
            
        Returns:
            list: Filtered list of tuples (filename, score)
        """
        filtered_results = [res for res in results if res[1] >= self.threshold]
        
        if not filtered_results and results:
             # If no results pass threshold, return top 3 with a warning flag implicit (or handle elsewhere)
             # For now, just return the top results even if low score.
             return results[:3]
        
        return filtered_results
