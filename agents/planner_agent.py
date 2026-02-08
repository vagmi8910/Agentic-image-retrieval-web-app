from .intent_agent import IntentAgent
from .refinement_agent import RefinementAgent
from .evaluator_agent import EvaluatorAgent
from ml.embed_text import embed_text
from ml.similarity import find_similar_images

class PlannerAgent:
    def __init__(self):
        self.intent_agent = IntentAgent()
        self.refinement_agent = RefinementAgent()
        self.evaluator_agent = EvaluatorAgent()

    def run(self, query, image_embeddings):
        """
        Orchestrates the retrieval process.
        """
        # Step 1: Understand Intent
        intent = self.intent_agent.extract_intent(query)
        print(f"Intent detected: {intent}")
        
        # Step 2: Refine Query
        refined_query = self.refinement_agent.refine_query(query)
        print(f"Refined query: {refined_query}")
        
        # Step 3: Embed Query
        query_embedding = embed_text(refined_query)
        
        # Step 4: Search
        results = find_similar_images(query_embedding, image_embeddings)
        
        # Step 5: Evaluate & Select Best
        final_results = self.evaluator_agent.evaluate_results(results)
        
        return final_results, intent
