import os


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
	print("Error: API key not found")
	raise ValueError("Gemini api key not found!")