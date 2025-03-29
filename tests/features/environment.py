# tests/features/environment.py

from src.utils.load_test_env import load_test_env

def before_all(context):
    context.env = load_test_env()
    print(f"[Behave] Loaded test env: {context.env}")