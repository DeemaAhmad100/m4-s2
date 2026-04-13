"""generate_chart.py - Interactive Executive KPI Dashboard"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os


city_data = {
    'City': ['Amman', 'Irbid', 'Zarqa', 'Aqaba', 'Unknown', 'Salt', 'Madaba'],
    'Revenue': [15780, 6820, 5210, 3940, 2890, 2150, 1910]
}
df_city = pd.DataFrame(city_data)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
monthly_revenue = [4200, 4800, 5100, 6300, 7200, 8900]
mom_growth = [5.2, 14.3, 6.25, 23.5, 14.3, 23.6]

categories = ['Books', 'Electronics', 'Clothing', 'Home & Garden', 'Food & Beverage', 'Sports']
cat_revenue = [11274, 11005, 10322, 7252, 4443.5, 4405]

# create subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Monthly Revenue Trend", 
                    "Month-over-Month Growth Rate",
                    "Revenue by Product Category", 
                    "Revenue by City - Amman Dominates"),
    vertical_spacing=0.20,
    horizontal_spacing=0.15
)

# 1. Monthly Revenue
fig.add_trace(go.Scatter(x=months, y=monthly_revenue, mode='lines+markers',
                         line=dict(width=4, color='#1E88E5'), name="Revenue"),
              row=1, col=1)

# 2. MoM Growth
fig.add_trace(go.Bar(x=months, y=mom_growth, marker_color='#26C6DA'), row=1, col=2)

# 3. Revenue by Category
fig.add_trace(go.Bar(x=cat_revenue, y=categories, orientation='h',
                     marker_color='#66BB6A'), row=2, col=1)

# 4. Revenue by City
colors = ['#90CAF9']*6 + ['#F4B400']
fig.add_trace(go.Bar(x=df_city['Revenue'], y=df_city['City'], orientation='h',
                     marker_color=colors), row=2, col=2)

# Improvements
fig.update_xaxes(title_text="Month", row=1, col=1)
fig.update_yaxes(title_text="Revenue (JOD)", row=1, col=1)

fig.update_xaxes(title_text="Growth (%)", row=1, col=2)
fig.update_yaxes(title_text="Month", row=1, col=2)

fig.update_xaxes(title_text="Revenue (JOD)", row=2, col=1)
fig.update_yaxes(title_text="Category", row=2, col=1)

fig.update_xaxes(title_text="Revenue (JOD)", row=2, col=2)
fig.update_yaxes(title_text="City", row=2, col=2)

# general design
fig.update_layout(
    height=1000,
    width=1450,
    title_text="Amman Digital Market - Executive KPI Overview<br>"
               "<span style='font-size:18px'>Total Revenue: 48,701.5 JOD | Q1 2026</span>",
    template="plotly_white",
    title_x=0.5,
    title_font_size=24
)

os.makedirs("output", exist_ok=True)
fig.write_html("output/executive_kpi_dashboard.html")
fig.write_image("chart.png", scale=3, width=1450, height=1000)

print("✅ the graph is ready!")
print("   → Interactive HTML: output/executive_kpi_dashboard.html")
print("   → Static Image   : chart.png")