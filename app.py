import streamlit as st
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(page_title="Wealth & Nest Egg Tracker", layout="wide")

# Modern UI Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    h1, h2, h3 {
        color: #1e293b;
        font-family: 'Inter', sans-serif;
    }
    div[data-testid="stMetricValue"] {
        font-size: 24px;
        color: #2563eb;
    }
    </style>
    """, unsafe_allow_実験=True)

st.title("Wealth & Nest Egg Tracker")
st.write("Calculate your annual cash flow and projected financial independence target.")

# Main Layout: Two columns (Input on Left, Results on Right)
input_col, results_col = st.columns([1, 1.2], gap="large")

with input_col:
    st.subheader("Monthly Expenses")
    
    # Using Expanders or Containers to keep the UI clean
    with st.container():
        housing = st.number_input("Housing (Mortgage/Rent, Tax, Insurance)", value=2500.0, step=100.0)
        transport = st.number_input("Transportation (Car, Gas, Insurance)", value=800.0, step=50.0)
        food = st.number_input("Food (Groceries & Dining)", value=1200.0, step=50.0)
        utilities = st.number_input("Utilities (Power, Water, Internet, Phone)", value=450.0, step=25.0)
        healthcare = st.number_input("Healthcare (Premiums & Out-of-pocket)", value=600.0, step=50.0)
        lifestyle = st.number_input("Lifestyle & Personal (Gym, Pets, Hobbies)", value=400.0, step=50.0)
        other = st.number_input("Other (Miscellaneous Catch-all)", value=250.0, step=25.0)

# Calculations
monthly_total = housing + transport + food + utilities + healthcare + lifestyle + other
annual_total = monthly_total * 12
nest_egg = annual_total * 25

with results_col:
    st.subheader("Financial Overview")
    
    # Metrics Row
    m_col1, m_col2 = st.columns(2)
    m_col1.metric("Annual Spending", f"${annual_total:,.0f}")
    m_col2.metric("Target Nest Egg", f"${nest_egg:,.0f}")

    # Modern Graphic Representation (Donut Chart)
    labels = ['Housing', 'Transport', 'Food', 'Utilities', 'Healthcare', 'Lifestyle', 'Other']
    values = [housing, transport, food, utilities, healthcare, lifestyle, other]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels, 
        values=values, 
        hole=.6,
        marker=dict(colors=['#1e40af', '#3b82f6', '#60a5fa', '#93c5fd', '#bfdbfe', '#dbeafe', '#f1f5f9']),
        textinfo='label+percent',
        showlegend=False
    )])
    
    fig.update_layout(
        margin=dict(t=0, b=0, l=0, r=0),
        height=350,
        annotations=[dict(text='Expense<br>Mix', x=0.5, y=0.5, font_size=20, showarrow=False)]
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # Context Note
    st.markdown(f"""
    ---
    ### 💡 The 25x Strategy
    To maintain a spend of **${annual_total:,.0f}/year** indefinitely, a portfolio of **${nest_egg:,.0f}** is required based on the 4% safe withdrawal rate. This assumes your investments are diversified 
    between equities and fixed income.
    """)

