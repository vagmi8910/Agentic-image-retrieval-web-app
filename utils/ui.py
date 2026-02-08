import streamlit as st
import base64
from io import BytesIO

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
            --glass-bg: rgba(15, 23, 42, 0.6); /* Dark semi-transparent background */
            --glass-border: rgba(255, 255, 255, 0.1);
            --text-main: #ffffff;
            --text-bright: #e2e8f0;
        }

        /* FORCE ALL TEXT TO BE WHITE/READABLE */
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

        /* --- INPUT FIELDS (SEARCH BOX FIX) --- */
        .stTextInput > div > div > input {
            background-color: #1e1e2e !important;  /* Dark background for contrast */
            color: #ffffff !important;             /* WHITE TEXT - High Visibility */
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 12px 16px;
            font-size: 1rem;
        }

        /* Styling when you click inside the box */
        .stTextInput > div > div > input:focus {
            background-color: #252540 !important;
            border-color: var(--primary-neon) !important;
            box-shadow: 0 0 15px rgba(0, 242, 255, 0.3);
            color: #ffffff !important;
        }

        /* Placeholder text color */
        .stTextInput input::placeholder {
            color: #94a3b8 !important;
            opacity: 0.8;
        }
        
        /* The Label above the input box */
        .stTextInput label {
            color: var(--primary-neon) !important;
            font-size: 1rem;
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

        /* --- RESULT CARD STYLING --- */
        .result-card {
            background: rgba(15, 23, 42, 0.8); /* Dark card background */
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
        
        .result-card p {
            color: #cbd5e1 !important; /* Light gray for subtitles */
            font-size: 0.9rem !important;
            margin: 0 !important;
        }

        .score-pill {
            background: var(--primary-neon);
            color: #000 !important; /* Black text on neon background */
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 800;
            font-size: 0.8rem;
            box-shadow: 0 0 10px var(--primary-neon);
        }

        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
    </style>
    """, unsafe_allow_html=True)

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
                <p style="margin: 0;">
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