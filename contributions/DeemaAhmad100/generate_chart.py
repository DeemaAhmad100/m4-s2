"""generate_chart.py - Multi-Panel with Gradient Colors"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# ====================== البيانات ======================
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
monthly_revenue = [4200, 4800, 5100, 6300, 7200, 8900]
mom_growth = [5.2, 14.3, 6.25, 23.5, 14.3, 23.6]

categories = ['Books', 'Electronics', 'Clothing', 'Home & Garden', 'Food & Beverage', 'Sports']
cat_revenue = [11274, 11005, 10322, 7252, 4443.5, 4405]

city_data = {
    'City': ['Amman', 'Irbid', 'Zarqa', 'Aqaba', 'Unknown', 'Salt', 'Madaba'],
    'Revenue': [15780, 6820, 5210, 3940, 2890, 2150, 1910]
}
df_city = pd.DataFrame(city_data)

# ====================== الرسمة الرئيسية (4 لوحات) ======================
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        "Monthly Revenue Trend",
        "Month-over-Month Growth Rate",
        "Revenue by Product Category",
        "Revenue by City - Amman Dominates"
    ),
    vertical_spacing=0.20,
    horizontal_spacing=0.15
)

# 1. Monthly Revenue Trend
fig.add_trace(go.Scatter(x=months, y=monthly_revenue, mode='lines+markers',
                         line=dict(width=4, color='#1E88E5')), row=1, col=1)

# 2. MoM Growth - Gradient Bars
colors_mom = ['#81D4FA', '#4FC3F7', '#29B6F6', '#03A9F4', '#0288D1', '#0277BD']
fig.add_trace(go.Bar(x=months, y=mom_growth, marker_color=colors_mom), row=1, col=2)

green_grad = ['#C8E6C9', '#A5D6A7', '#81C784', '#66BB6A', '#4CAF50', '#388E3C']
fig.add_trace(go.Bar(x=cat_revenue, y=categories, orientation='h',
                     marker_color=green_grad), row=2, col=1)

blue_grad = ['#BBDEFB', '#81D4FA', '#4FC3F7', '#29B6F6', '#03A9F4', '#0288D1', '#0277BD']
fig.add_trace(go.Bar(x=df_city['Revenue'], y=df_city['City'], orientation='h',
                     marker_color=blue_grad), row=2, col=2)

fig.add_trace(go.Bar(x=[15780], y=['Amman'], orientation='h',
                     marker_color='#F4B400'), row=2, col=2)

fig.update_yaxes(title_text="Month", row=1, col=2)

fig.update_xaxes(title_text="Revenue (JOD)", row=2, col=1)
fig.update_yaxes(title_text="Category", row=2, col=1)

fig.update_xaxes(title_text="Revenue (JOD)", row=2, col=2)
fig.update_yaxes(title_text="City", row=2, col=2)

fig.update_layout(
    height=980,
    width=1480,
    title_text="Amman Digital Market - Executive KPI Overview<br>"
               "<span style='font-size:16px'>Total Revenue: 48,701.5 JOD | Q1 2026</span>",
    template="plotly_white",
    title_x=0.5,
    title_font_size=22,
    showlegend=False
)

os.makedirs("output", exist_ok=True)
fig.write_html("output/executive_kpi_dashboard.html")
fig.write_image("chart.png", scale=3, width=1480, height=980)

print("Dashboard generated successfully!")
print("   → Interactive HTML: output/executive_kpi_dashboard.html")
print("   → Static Image     : chart.png")