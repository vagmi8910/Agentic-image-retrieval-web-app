import streamlit as st
import os
from PIL import Image
from agents.planner_agent import PlannerAgent
from ml.embed_images import embed_images
from utils.file_utils import load_embeddings, save_embeddings
from utils.ui import load_custom_css, display_result_card

# --- Constants ---
IMAGE_DIR = "data/images"
EMBEDDINGS_PATH = "embeddings/image_embeddings.pkl"

# --- Setup ---
os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(os.path.dirname(EMBEDDINGS_PATH), exist_ok=True)

st.set_page_config(page_title="Agentic Image Retrieval", layout="wide")
load_custom_css()

# --- Helper Functions ---
@st.cache_resource
def get_planner_agent():
    return PlannerAgent()

def load_system_embeddings():
    """Load embeddings from disk or generate if missing."""
    embeddings = load_embeddings(EMBEDDINGS_PATH)
    
    # Check for dimension mismatch (ViT-L-14 should be 768)
    if embeddings:
        first_emb = next(iter(embeddings.values()))
        if first_emb.shape[-1] != 768:
            st.warning("⚠️ Detected incompatible embeddings (likely from older model). Clearing index...")
            embeddings = {}
            try:
                os.remove(EMBEDDINGS_PATH)
            except OSError:
                pass

    if not embeddings:
        st.warning("No embeddings found. Please add images to get started.")
    return embeddings

def update_embeddings_index():
    """Re-runs embedding generation for all images."""
    with st.spinner("Updating image index... (this may take a moment)"):
        embeddings = embed_images(IMAGE_DIR)
        save_embeddings(embeddings, EMBEDDINGS_PATH)
    return embeddings

# --- Main UI ---
def main():
    st.title("🧠 Agentic Image Retrieval System 🤖")
    st.markdown("🧩 Use natural language to find images.")

    # --- Sidebar: Image Management ---
    with st.sidebar:
        st.header("📤 Upload Images")
        st.markdown("📷 Add images to your search index here.")
        
        uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True, type=['jpg', 'jpeg', 'png'])
        
        if uploaded_files:
            if st.button(f"Add {len(uploaded_files)} Images to Index"):
                with st.spinner("📷 Processing images..."):
                    for uploaded_file in uploaded_files:
                        path = os.path.join(IMAGE_DIR, uploaded_file.name)
                        with open(path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                    
                    # Update embeddings after upload
                    embeddings = update_embeddings_index()
                    st.session_state['embeddings'] = embeddings
                    st.success(f"✅ Successfully added {len(uploaded_files)} images!")
                    st.rerun()

        st.divider()
        if st.button("🔄 Refresh Index"):
            embeddings = update_embeddings_index()
            st.session_state['embeddings'] = embeddings
            st.success("Index refreshed!")

    # --- Load Embeddings ---
    if 'embeddings' not in st.session_state:
        st.session_state['embeddings'] = load_system_embeddings()
    
    embeddings = st.session_state['embeddings']
    
    if not embeddings:
         st.info("🖼️ Please upload images in the sidebar to begin.")
         return

    # --- Search Section ---
    query = st.text_input("Describe the image you are looking for:", placeholder="e.g., a red sports car on a mountain road")
    
    if st.button("Search") or query:
        if not query.strip():
            st.warning("Please enter a query.")
        else:
            planner = get_planner_agent()
            
            with st.spinner("🚀 Agents are working..."):
                # Run Agentic Pipeline
                results, intent = planner.run(query, embeddings)
            
            # --- Display Results ---
            st.subheader("Results")
            if not results:
                st.warning("⚠️ No relevant images found matching your criteria.")
            else:
                # Display top 3 results in columns
                cols = st.columns(len(results))
                for idx, (filename, score) in enumerate(results):
                    with cols[idx]:
                        image_path = os.path.join(IMAGE_DIR, filename)
                        try:
                            image = Image.open(image_path)
                            display_result_card(idx, image, filename, score)
                        except Exception as e:
                            st.error(f"Could not load image {filename}")

if __name__ == "__main__":
    main()
