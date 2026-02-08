try:
    from agents.planner_agent import PlannerAgent
    from ml.clip_model import CLIPModel
    print("Imports successful!")
except ImportError as e:
    print(f"Import failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
