# scripts/launch_review.py
import subprocess

def run_review_ui():
    subprocess.run(["streamlit", "run", "src/review/review_streamlit.py"])

if __name__ == "__main__":
    run_review_ui()