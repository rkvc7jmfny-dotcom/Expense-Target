import streamlit as st
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(page_title="Expenses & Nest Egg Estimator", layout="wide")

# Modern UI Styling with Dynamic Scaling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    
    /* Responsive Metric Container */
    .metric-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Label Styling */
    .metric-label {
        color: #2563eb;
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* DYNAMIC TEXT SIZE: Scales with viewport width */
    .metric-value {
        color: #2563eb;
        font-weight: 800;
        font-size: clamp(1.5rem, 2.5vw, 3rem); /* Min 1.5rem, Scales at 2.5% of width, Max 3rem */
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .blue-header {
        color: #2563eb !important;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #2563eb;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Expense & Nest Egg Estimator")
st.write("Calculate your annual cash flow and projected financial independence target.")

# Main Layout
input_col, results_col = st.columns([1, 1.2], gap="large")

with input_col:
    st.subheader("Monthly Expenses")
    housing = st.number_input("Housing (Mortgage/Rent, Tax, Insurance)", value=2500.0, step=100.0)
    transport = st.number_input("Transportation (Car, Gas, Insurance)", value=800.0, step=50.0)
    food = st.number_input("Food (Groceries & Dining)", value=1200.0, step=50.0)
    utilities = st.number_input("Utilities (Power, Water, Internet, Phone)", value=450.0, step=25.0)
    healthcare = st.number_input("Healthcare (Premiums & Out-of-pocket)", value=600.0, step=50.0)
    lifestyle = st.number_input("Lifestyle & Personal (Gym, Pets, Hobbies)", value=400.0, step=50.0)
    shopping = st.number_input("Shopping (Clothing, Electronics, Home Goods)", value=300.0, step=50.0)
    debt = st.number_input("Credit Debt (Monthly Payments)", value=200.0, step=50.0)
    vacation = st.number_input("Vacation/Travel (Annual Budget / 12)", value=400.0, step=50.0)
    other = st.number_input("Other (Miscellaneous Catch-all)", value=250.0, step=25.0)

# Calculations
monthly_total = housing + transport + food + utilities + healthcare + lifestyle + shopping + debt + vacation + other
annual_total = monthly_total * 12
nest_egg = annual_total * 25

with results_col:
    st.markdown('<h3 class="blue-header">Financial Overview</h3>', unsafe_allow_html=True)
    
    # Custom Responsive Metrics
    m_col1, m_col2 = st.columns(2)
    
    m_col1.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Annual Spending</div>
            <div class="metric-value">${annual_total:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)
    
    m_col2.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Target Nest Egg</div>
            <div class="metric-value">${nest_egg:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)

    # Donut Chart
    labels = ['Housing', 'Transport', 'Food', 'Utilities', 'Healthcare', 'Lifestyle', 'Shopping', 'Debt', 'Vacation', 'Other']
    values = [housing, transport, food, utilities, healthcare, lifestyle, shopping, debt, vacation, other]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels, 
        values=values, 
        hole=.6,
        marker=dict(colors=['#1e3a8a', '#1e40af', '#2563eb', '#3b82f6', '#60a5fa', '#93c5fd', '#bfdbfe', '#dbeafe', '#eff6ff', '#f8fafc']),
        textinfo='percent',
        hoverinfo='label+value'
    )])
    
    fig.update_layout(
        margin=dict(t=30, b=0, l=0, r=0),
        height=450,
        annotations=[dict(text='Expense<br>Mix', x=0.5, y=0.5, font_size=20, showarrow=False, font_color="#2563eb")],
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5, font=dict(color="#2563eb"))
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # Adaptive Blue Commentary Box
    st.markdown(f"""
    <div style="background-color: #eff6ff; padding: 20px; border-radius: 10px; border-left: 5px solid #2563eb; margin-top: 20px;">
        <h4 style="margin-top:0; color: #2563eb;">💡 The 25x Strategy</h4>
        <p style="color: #2563eb; font-size: clamp(0.9rem, 1.2vw, 1.1rem);">
            To sustain an annual spend of <b style="font-size: 1.2em;">${annual_total:,.0f}</b>, 
            you need a total nest egg of <b style="font-size: 1.2em;">${nest_egg:,.0f}</b>.
        </p>
        <p style="color: #2563eb; font-size: 0.85em; opacity: 0.8;">
            Based on the 4% Rule (Trinity Study) for long-term portfolio sustainability.
        </p>
    </div>
    """, unsafe_allow_html=True)
