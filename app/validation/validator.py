def validate_financials(data):

    errors = []

    try:

        assets = data["balance_sheet"]["total_assets"]
        liabilities = data["balance_sheet"]["total_liabilities"]
        equity = data["balance_sheet"]["equity"]

        net_income = data["income_statement"]["net_income"]
        operating_cf = data["cash_flow"]["operating_cash_flow"]

        if assets != liabilities + equity:
            errors.append("Balance Sheet does NOT balance.")

        if net_income > 0 and operating_cf < 0:
            errors.append("Company shows profit but negative operating cash flow.")

        
        if equity < 0:
            errors.append("Negative shareholder equity detected.")

        
        if equity != 0:
            debt_to_equity = liabilities / equity
            if debt_to_equity > 3:
                errors.append("High debt-to-equity ratio (>3).")

    except Exception as e:
        errors.append(f"Validation error: {str(e)}")

    return errors