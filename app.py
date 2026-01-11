import streamlit as st

st.set_page_config(page_title="Family Wealth & Nest Egg Tracker", layout="centered")

st.title("👨‍👩‍👧‍👦 Family Expense & Nest Egg Calculator")
st.write("Determine your annual spending and the 'FIRE' number needed for financial independence.")

# Sidebar for logic constants
st.sidebar.header("Calculation Assumptions")
inflation_rate = st.sidebar.slider("Assumed Inflation (%)", 1.0, 5.0, 3.0) / 100
years_to_retirement = st.sidebar.number_input("Years until retirement", min_value=1, value=20)
multiplier = 25 # The 4% Rule

# 1. Input Section
st.header("1. Monthly Expenses")
col1, col2 = st.columns(2)

with col1:
    housing = st.number_input("Housing (Mortgage/Rent, Tax, Insurance)", min_value=0.0, value=2000.0)
    transport = st.number_input("Transportation (Car, Gas, Insurance)", min_value=0.0, value=800.0)
    food = st.number_input("Food (Groceries & Dining)", min_value=0.0, value=1000.0)
    utilities = st.number_input("Utilities (Power, Water, Phone, Net)", min_value=0.0, value=400.0)

with col2:
    healthcare = st.number_input("Healthcare (Premiums & Medical)", min_value=0.0, value=500.0)
    family = st.number_input("Family (Childcare, School, Activities)", min_value=0.0, value=600.0)
    lifestyle = st.number_input("Lifestyle (Subscriptions, Pets, Gym)", min_value=0.0, value=300.0)
    other = st.number_input("Other (Miscellaneous/Catch-all)", min_value=0.0, value=200.0)

# 2. Calculations
monthly_total = housing + transport + food + utilities + healthcare + family + lifestyle + other
annual_total = monthly_total * 12
nest_egg_today = annual_total * multiplier

# Future value of money formula: FV = PV * (1 + r)^n
nest_egg_future = nest_egg_today * ((1 + inflation_rate) ** years_to_retirement)

st.divider()

# 3. Display Results
st.header("2. Your Results")

m1, m2 = st.columns(2)
m1.metric("Total Monthly Expenses", f"${monthly_total:,.2f}")
m2.metric("Total Annual Expenses", f"${annual_total:,.2f}")

st.subheader(f"🎯 Your Nest Egg Goal: ${nest_egg_today:,.2f}")
st.write(f"Based on the **25x Rule**, you need this amount in **today's dollars** to retire safely.")

st.info(f"💡 **Adjusted for Inflation:** In {years_to_retirement} years (at {inflation_rate:.1%} inflation), your target nest egg becomes **${nest_egg_future:,.2f}**.")

# 4. Expense Breakdown Chart
st.write("---")
st.write("### Expense Breakdown")
chart_data = {
    "Housing": housing,
    "Transport": transport,
    "Food": food,
    "Utilities": utilities,
    "Healthcare": healthcare,
    "Family": family,
    "Lifestyle": lifestyle,
    "Other": other
}
st.bar_chart(chart_data)
