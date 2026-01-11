import streamlit as st
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(page_title="Wealth & Nest Egg Tracker", layout="wide")

# Custom CSS for high-quality, sophisticated UI
st.markdown("""
    <style>
    /* Main background and font */
    .stApp {
        background-color: #F8FAFC;
    }
    h1, h2, h3 {
        color: #1E293B;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }
    /* Metric Card Styling */
    [data-testid="stMetricValue"] {
        color: #059669; /* Soft Green */
        font-size: 32px;
    }
    /* Custom container for results */
    .results-container {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-left: 5px solid #3B82F6; /* Light Blue accent */
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Wealth & Nest Egg Tracker")
st.write("An intuitive dashboard for long-term financial independence.")

# Create two main columns for the side-by-side layout
input_col, display_col = st.columns([1, 1.2], gap="large")

with input_col:
    st.subheader("Monthly Expenses")
    
    # Using expanders to group subcategories for "Attention to Detail"
    with st.expander("🏠 Housing & Utilities", expanded=True):
        housing = st.number_input("Mortgage / Rent", value=2200.0, step=50.0)
        utilities = st.number_input("Utilities & Connectivity", value=400.0, step=10.0)
        
    with st.expander("🚗 Transportation", expanded=True):
        transport = st.number_input("Vehicles, Gas & Insurance", value=850.0, step=50.0)
        
    with st.expander("🥗 Daily Living", expanded=True):
        food = st.number_input("Food & Dining", value=1100.0, step=50.0)
        lifestyle = st.number_input("Lifestyle & Personal Care", value=400.0, step=10.0)
        
    with st.expander("🏥 Healthcare & Others", expanded=True):
        healthcare = st.number_input("Medical & Insurance", value=500.0, step=10.0)
        other = st.number_input("Other (Catch-all)", value=250.0, step=10.0)

# Calculations
monthly_total = housing + utilities + transport + food + lifestyle + healthcare + other
annual_total = monthly_total * 12
nest_egg = annual_total * 25

with display_col:
    st.subheader("Financial Summary")
    
    # Results Box
    st.markdown('<div class="results-container">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.metric("Annual Spend", f"${annual_total:,.0f}")
    c2.metric("Target Nest Egg", f"${nest_egg:,.0f}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("---")
    
    # Modern Graphic Representation (Plotly Donut Chart)
    labels = ['Housing', 'Utilities', 'Transport', 'Food', 'Lifestyle', 'Healthcare', 'Other']
    values = [housing, utilities, transport, food, lifestyle, healthcare, other]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels, 
        values=values, 
        hole=.5,
        marker=dict(colors=['#1E3A8A', '#3B82F6', '#60A5FA', '#34D399', '#10B981', '#059669', '#94A3B8']),
        textinfo='percent'
    )])
    
    fig.update_layout(
        margin=dict(t=0, b=0, l=0, r=0),
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        annotations=[dict(text='Expenses', x=0.5, y=0.5, font_size=20, showarrow=False)]
    )
    
    st.plotly_chart(fig, use_container_width=True)

    st.success(f"To sustain a lifestyle of **${annual_total:,.0f}/year**, your capital target is **${nest_egg:,.0f}**.")
