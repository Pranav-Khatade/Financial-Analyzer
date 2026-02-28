import json
from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def normalize_json(raw_json):

    prompt = f"""
    You are a Financial Data normalization system.
    Convert the following JSON input into EXACT format below.

    {{
      "income_statement": {{
        "revenue": number,
        "cogs": number,
        "operating_expense": number,
        "net_income": number
      }},
      "balance_sheet": {{
        "total_assets": number,
        "total_liabilities": number,
        "equity": number
      }},
      "cash_flow": {{
        "operating_cash_flow": number,
        "investing_cash_flow": number,
        "financing_cash_flow": number
      }}
    }}

    Rules:
    - Return ONLY valid JSON.
    - If a field is missing, use 0.
    - Do not explain anything.

    Input JSON:
    {json.dumps(raw_json)}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    cleaned_output = response.text.strip()

  
    if cleaned_output.startswith("```"):
        cleaned_output = cleaned_output.replace("```json", "").replace("```", "").strip()

    return json.loads(cleaned_output)