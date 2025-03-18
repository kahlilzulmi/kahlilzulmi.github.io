# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 12:25:05 2025

@author: admin
"""

import pandas as pd
import plotly.express as px

# Step 1: Read data from Excel
df = pd.read_excel("datanalis.xlsx")

# Step 2: Create GeoChart
fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="Value",
    hover_name="Country",
    title="GeoChart Example",
    color_continuous_scale=px.colors.sequential.Plasma,
    scope="world",
    projection="natural earth"
)

# Step 3: Show the chart
fig.show()

# Step 4: Save the chart (optional)
fig.write_html("geochart.html")
fig.write_image("geochart.png")