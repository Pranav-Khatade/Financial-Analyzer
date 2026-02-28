import matplotlib.pyplot as plt
import os

def save_financial_graphs(data):

    os.makedirs("reports", exist_ok=True)

    revenue = data["income_statement"]["revenue"]
    net_income = data["income_statement"]["net_income"]

    plt.figure()
    plt.bar(["Revenue", "Net Income"], [revenue, net_income])
    plt.title("Revenue vs Net Income")
    plt.tight_layout()
    plt.savefig("reports/revenue_vs_income.png")
    plt.close()

    liabilities = data["balance_sheet"]["total_liabilities"]
    equity = data["balance_sheet"]["equity"]

    plt.figure()
    plt.bar(["Liabilities", "Equity"], [liabilities, equity])
    plt.title("Debt vs Equity")
    plt.tight_layout()
    plt.savefig("reports/debt_vs_equity.png")
    plt.close()

    operating_cf = data["cash_flow"]["operating_cash_flow"]
    investing_cf = data["cash_flow"]["investing_cash_flow"]
    financing_cf = data["cash_flow"]["financing_cash_flow"]

    plt.figure()
    plt.bar(
        ["Operating", "Investing", "Financing"],
        [operating_cf, investing_cf, financing_cf]
    )
    plt.title("Cash Flow Breakdown")
    plt.tight_layout()
    plt.savefig("reports/cash_flow_breakdown.png")
    plt.close()

    return {
        "rev_income": "reports/revenue_vs_income.png",
        "debt_equity": "reports/debt_vs_equity.png",
        "cash_flow": "reports/cash_flow_breakdown.png"
    }