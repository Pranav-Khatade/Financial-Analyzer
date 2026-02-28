from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_insights(ratios, validation_errors):

    prompt = f"""
    You are a professional financial analyst.

    Below are financial ratios and validation results of a company.

    Financial Ratios:
    {ratios}

    Validation Issues:
    {validation_errors}

    Your task:
    1. Analyze overall financial health.
    2. Identify major strengths.
    3. Identify risks or weaknesses.
    4. Suggest practical improvements.
    5. Comment on leverage and profitability.
    
    Be concise but professional.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text