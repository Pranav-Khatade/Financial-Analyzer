def calculate_risk_score(ratios, validation_errors):

    score = 0

    if "Debt to Equity" in ratios and ratios["Debt to Equity"] > 3:
        score += 25

    if "Operating CF to Net Income" in ratios and ratios["Operating CF to Net Income"] < 0.5:
        score += 20

    if validation_errors:
        score += 20

    if "ROE" in ratios and ratios["ROE"] < 0.1:
        score += 15

    score = min(score, 100)

    if score < 30:
        level = "Low Risk"
    elif score < 60:
        level = "Moderate Risk"
    else:
        level = "High Risk"

    return score, level