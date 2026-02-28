import json
import os

def load_json_file(file_path):


    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if not file_path.endswith(".json"):
        raise ValueError("Only .json files are supported.")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format.")

    return data