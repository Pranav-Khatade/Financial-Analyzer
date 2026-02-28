def compute_ratios(data):

    ratios = {}

    try:
        revenue = data["income_statement"]["revenue"]
        net_income = data["income_statement"]["net_income"]
        assets = data["balance_sheet"]["total_assets"]
        liabilities = data["balance_sheet"]["total_liabilities"]
        equity = data["balance_sheet"]["equity"]
        operating_cf = data["cash_flow"]["operating_cash_flow"]

        if revenue != 0:
            ratios["Net Margin"] = round(net_income / revenue, 4)

        if assets != 0:
            ratios["ROA"] = round(net_income / assets, 4)

        if equity != 0:
            ratios["ROE"] = round(net_income / equity, 4)

        if equity != 0:
            ratios["Debt to Equity"] = round(liabilities / equity, 4
)
        if net_income != 0:
            ratios["Operating CF to Net Income"] = round(operating_cf / net_income, 4)

    except Exception as e:
        ratios["Error"] = str(e)

    return ratios