import streamlit as st
import base64
from io import BytesIO
from PIL import Image

# -----------------------------------------------------------------------------
# 1. SETUP & STYLE LOADING
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Neon Image Search", layout="wide")

def load_custom_css():
    """
    Injects the final updated CSS for a high-contrast, Neon Glassmorphism theme.
    """
    st.markdown("""
    <style>
        /* Import premium font */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

        :root {
            --bg-dark: #0a0a0f;
            --primary-neon: #00f2ff; /* Cyan Neon */
            --secondary-neon: #ff007f; /* Hot Pink Neon */
            --glass-bg: rgba(15, 23, 42, 0.6);
            --glass-border: rgba(255, 255, 255, 0.1);
            --text-main: #ffffff;
        }

        /* FORCE ALL TEXT TO BE WHITE */
        html, body, [class*="css"], .stApp {
            font-family: 'Outfit', sans-serif;
            color: var(--text-main) !important;
        }

        /* --- BACKGROUND ANIMATION --- */
        .stApp {
            background: linear-gradient(-45deg, #050505, #1a1a2e, #16213e, #0f0c29);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
        }
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* --- HEADINGS --- */
        h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: white !important;
            text-shadow: 0 0 15px rgba(0, 242, 255, 0.4);
            font-weight: 800 !important;
            letter-spacing: -1px;
        }

        /* --- SIDEBAR --- */
        [data-testid="stSidebar"] {
            background-color: #05050a;
            border-right: 1px solid var(--glass-border);
        }
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
            color: #ffffff !important;
        }

        /* --- INPUT FIELDS & SEARCH BOX --- */
        .stTextInput > div > div > input {
            background-color: #1e1e2e !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 12px 16px;
        }
        .stTextInput > div > div > input:focus {
            background-color: #252540 !important;
            border-color: var(--primary-neon) !important;
            box-shadow: 0 0 15px rgba(0, 242, 255, 0.3);
            color: #ffffff !important;
        }
        .stTextInput label {
            color: var(--primary-neon) !important;
            font-size: 1rem;
            font-weight: 700;
        }

        /* --- FILE UPLOADER FIX (CRITICAL) --- */
        [data-testid="stFileUploader"] {
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px dashed var(--primary-neon);
            border-radius: 15px;
            padding: 20px;
        }
        [data-testid="stFileUploader"] section {
            background-color: transparent !important;
        }
        /* The text "Drag and drop file here" */
        [data-testid="stFileUploader"] span {
            color: white !important; 
        }
        /* The "Browse files" button */
        [data-testid="stFileUploader"] button {
            background: var(--primary-neon);
            color: black !important;
            border: none;
            font-weight: 700;
        }

        /* --- BUTTONS --- */
        .stButton > button {
            background: linear-gradient(135deg, var(--secondary-neon) 0%, #7000ff 100%);
            border: none;
            color: white !important;
            padding: 0.6rem 1.5rem;
            border-radius: 50px;
            font-weight: 700;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 25px rgba(255, 0, 127, 0.6);
        }

        /* --- RESULT CARD --- */
        .result-card {
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 16px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            transition: transform 0.3s ease;
        }
        .result-card:hover {
            transform: translateY(-5px);
            border-color: var(--primary-neon);
            box-shadow: 0 0 20px rgba(0, 242, 255, 0.2);
        }
        .result-card h4 {
            color: #ffffff !important;
            font-weight: 700;
            margin: 10px 0 5px 0 !important;
        }
        .score-pill {
            background: var(--primary-neon);
            color: #000 !important;
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 800;
            font-size: 0.8rem;
            box-shadow: 0 0 10px var(--primary-neon);
        }

        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
    </style>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def img_to_base64(image):
    """Converts a PIL Image to a base64 string."""
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

def display_result_card(idx, image, filename, score):
    """
    Renders a high-visibility, neon-styled result card with full images and download button.
    """
    img_str = img_to_base64(image)
    score_percent = score * 100
    
    html_code = f"""
    <div class="result-card">
        <div style="position: relative; background: rgba(0,0,0,0.3); border-radius: 12px;">
            <img src="data:image/jpeg;base64,{img_str}" 
                 style="border-radius: 12px; width: 100%; height: 300px; object-fit: contain; display: block; border: 1px solid rgba(255,255,255,0.1);">
            <div style="position: absolute; top: 10px; right: 10px;">
                <span class="score-pill">{score_percent:.1f}% Match</span>
            </div>
        </div>
        <div style="padding: 10px 5px 0 5px;">
            <h4 style="overflow: hidden; white-space: nowrap; text-overflow: ellipsis; margin-bottom: 5px;" title="{filename}">
                {filename}
            </h4>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <p style="margin: 0; color: #cbd5e1; font-size: 0.9rem;">
                    <span style="color: #00f2ff;">●</span> Image ID: {idx}
                </p>
                <a href="data:image/jpeg;base64,{img_str}" download="{filename}" style="text-decoration: none;">
                    <button style="
                        background: linear-gradient(90deg, #00f2ff, #0099ff);
                        border: none;
                        color: #000;
                        padding: 6px 14px;
                        border-radius: 15px;
                        font-weight: 700;
                        font-family: 'Outfit', sans-serif;
                        font-size: 0.8rem;
                        cursor: pointer;
                        box-shadow: 0 0 10px rgba(0, 242, 255, 0.4);
                        transition: all 0.2s;
                    ">
                        ⬇ Download
                    </button>
                </a>
            </div>
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. MAIN APP LOGIC (The part that makes the drop-down visible)
# -----------------------------------------------------------------------------

def main():
    load_custom_css()

    st.title("⚡ Neon Image Retrieval")
    st.markdown("Upload an image below to find similar matches from the database.")

    # --- SIDEBAR (Where upload usually lives) ---
    with st.sidebar:
        st.header("Upload Query")
        
        # This is the File Uploader (Drop-down menu)
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            # Display preview of uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption='Query Image', use_container_width=True)
            
            # Button to trigger search
            if st.button("🔍 Search Database"):
                st.session_state['searching'] = True
                # Here you would call your backend search function
                # results = your_search_function(image)

    # --- MAIN CONTENT AREA ---
    
    # Example Logic: If user uploaded, show results. 
    # REPLACE THIS MOCK DATA WITH YOUR REAL BACKEND LOGIC
    if uploaded_file is not None and st.session_state.get('searching'):
        st.subheader("Results Found")
        
        # Creating columns for grid layout
        col1, col2, col3 = st.columns(3)
        
        # Mock Results (Delete this when connecting to your real model)
        # Using the uploaded image just to demonstrate the card display
        mock_img = Image.open(uploaded_file) 
        
        with col1:
            display_result_card(101, mock_img, "found_result_1.jpg", 0.98)
        with col2:
            display_result_card(102, mock_img, "found_result_2.jpg", 0.85)
        with col3:
            display_result_card(103, mock_img, "found_result_3.jpg", 0.72)

    elif uploaded_file is None:
        st.info("👋 Please upload an image in the sidebar to start searching.")

if __name__ == "__main__":
    main()
