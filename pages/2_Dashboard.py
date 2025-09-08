import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# ------------------------------
# Load Data
# ------------------------------

accounts_df = pd.read_csv('Account.csv')
chequings_tx_df = pd.read_csv('Cq_transactions.csv')
credit_tx_df = pd.read_csv('Credit_transactions.csv')

# Convert dates to datetime for filtering
chequings_tx_df['date'] = pd.to_datetime(chequings_tx_df['date'])
credit_tx_df['date'] = pd.to_datetime(credit_tx_df['date'])

# ------------------------------
# Dashboard Layout
# ------------------------------

st.set_page_config(page_title="Account Dashboard", layout="wide")
st.title("🪙 Sublime for Business Dashboard")

# ------------------------------
# Graphs
# ------------------------------


st.subheader("📊 Summary")

# Chequings – sum of positive amounts (money earned)
total_earned = chequings_tx_df[chequings_tx_df['amount'] > 0]['amount'].sum()

# Chequings – sum of negative amounts (spending)
total_spent_chequings = chequings_tx_df[chequings_tx_df['amount'] < 0]['amount'].sum()

# Credit – sum of positive amounts (spending via purchases)
total_spent_credit = credit_tx_df[credit_tx_df['amount'] > 0]['amount'].sum()

# Calculate total spent combined
total_spent = (-total_spent_chequings) + total_spent_credit  # negate chequings spent to display positive

# Display metrics side by side
col1, col2 = st.columns(2)
col1.metric("Total Earned", f"${total_earned:,.2f}")
col2.metric("Total Money Spent", f"${total_spent:,.2f}")

st.subheader("Your live insights")

# Create two columns for first two graphs
col1, col2 = st.columns(2)

# Graph 1: Chequings Spending Over Time
with col1:
    chequings_tx_df_spent = chequings_tx_df[chequings_tx_df['amount'] < 0].copy()
    chequings_tx_df_spent['amount'] = -chequings_tx_df_spent['amount']  # Convert to positive for graphing
    fig1 = px.line(chequings_tx_df_spent, x='date', y='amount', title='Chequings Spending Over Time')
    st.plotly_chart(fig1, use_container_width=True)

# Graph 2: Credit Spending Over Time
with col2:
    st.write("**Credit Spending Over Time**")
    fig2 = px.scatter(
        credit_tx_df,
        x='date',
        y='amount',
        title='Credit Spending Over Time',
        labels={'amount': 'Amount ($)', 'date': 'Date'}
    )
    st.plotly_chart(fig2, use_container_width=True)

# Graph 3: Vendors with Most Money Spent (full width underneath)
top_vendors = chequings_tx_df.groupby('vendor')['amount'].sum().sort_values().head(10).abs()  # top 10 negative (spent), absolute for display
fig3 = px.bar(top_vendors, x=top_vendors.index, y=top_vendors.values, title='Chequings transactions volume')
st.plotly_chart(fig3, use_container_width=True)


# ------------------------------
# Mercury AI Advisory Prompt
# ------------------------------

st.markdown("---")
st.subheader("🧠 Explore Deeper Insights with Mercury")
st.write("Gain tailored financial advice, identify opportunities, and optimize cash flow with Mercury, your interactive financial analysis AI.")

if st.button("Ask Mercury 💬"):
    st.write("🔧 Mercury is under development.")

# ------------------------------
# End of Dashboard
# ------------------------------
