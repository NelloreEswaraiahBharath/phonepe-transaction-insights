def generate_insights(df):
    insights = []

    # Top State
    top_state = df.groupby('State')['Amount'].sum().idxmax()
    insights.append(f"Top performing state is {top_state}")

    # Top Payment Type
    top_payment = df.groupby('Payment_Type')['Amount'].sum().idxmax()
    insights.append(f"Most used payment method is {top_payment}")

    # Growth Trend
    yearly = df.groupby('Year')['Amount'].sum()
    if yearly.iloc[-1] > yearly.iloc[0]:
        insights.append("Transactions are growing year over year")

    return insights
