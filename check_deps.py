import sys
try:
    import torch
    import open_clip
    with open("dep_check.txt", "w") as f:
        f.write(f"SUCCESS: torch={torch.__version__}, open_clip={open_clip.__version__}")
except ImportError as e:
    with open("dep_check.txt", "w") as f:
        f.write(f"FAILURE: {e}")
except Exception as e:
    with open("dep_check.txt", "w") as f:
        f.write(f"ERROR: {e}")
