# Agentic Image Retrieval System

A local, open-source image retrieval system using Vision-Language models (OpenCLIP) and an agentic pipeline to understand user intent and retrieve relevant images.

## Features

- **Natural Language Search**: Describe an image to find it.
- **Agentic Pipeline**:
    - **Intent Agent**: Understands what the user is looking for.
    - **Refinement Agent**: Optimizes the query for the model.
    - **Evaluator Agent**: Scores and selects the best matches.
- **Privacy-First**: Runs entirely locally. No external APIs.
- **Interactive UI**: Built with Streamlit.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

3. **Add Images**:
   Use the **Upload Images** section in the sidebar to add images to the index.

## Architecture

- **Frontend**: Streamlit
- **Backend**: Python
- **ML Model**: OpenCLIP (`ViT-L-14`)
- **Embeddings**: Stored as Pickle files in `embeddings/`

## Agents

1. **Intent Agent**: Extracts key concepts (Objects, Actions).
2. **Planner Agent**: Orchestrates the retrieval process.
3. **Refinement Agent**: Expands queries (e.g., "cat" -> "a photo of a cat").
4. **Evaluator Agent**: Filters low-confidence results.
