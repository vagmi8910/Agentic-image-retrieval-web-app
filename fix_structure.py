import os
import shutil
import sys

SOURCE_DIR = "agentic-image-retrieval"
TARGET_DIR = "."
DIRS_TO_MOVE = ["agents", "ml", "utils", "data", "embeddings"]
LOG_FILE = "debug_log.txt"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")
    print(msg)
    sys.stdout.flush()

def fix_structure():
    log(f"--- Starting Fix Structure ---")
    log(f"Python executable: {sys.executable}")
    log(f"Current working directory: {os.getcwd()}")
    
    if not os.path.exists(SOURCE_DIR):
        log(f"Directory '{SOURCE_DIR}' not found.")
        return

    try:
        log(f"Contents of '{SOURCE_DIR}': {os.listdir(SOURCE_DIR)}")
    except Exception as e:
        log(f"Error listing '{SOURCE_DIR}': {e}")
        return

    for directory in DIRS_TO_MOVE:
        src = os.path.join(SOURCE_DIR, directory)
        dst = os.path.join(TARGET_DIR, directory)
        
        log(f"Processing '{directory}'...")
        if os.path.exists(src):
            log(f"Copying '{src}' to '{dst}'...")
            try:
                if os.path.exists(dst):
                    log(f"Destination '{dst}' exists. Removing it first.")
                    if os.path.isdir(dst):
                        shutil.rmtree(dst)
                    else:
                        os.remove(dst)
                shutil.copytree(src, dst, dirs_exist_ok=True)
                log(f"Successfully copied '{directory}'.")
            except Exception as e:
                log(f"Error copying '{directory}': {e}")
        else:
            log(f"Source '{src}' not found.")

    # Check if app.py exists in root
    if os.path.exists("app.py"):
        log("app.py found in root.")
    else:
        log("app.py NOT found in root.")

if __name__ == "__main__":
    fix_structure()
