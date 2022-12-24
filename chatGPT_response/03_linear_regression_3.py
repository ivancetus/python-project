# input: plot a linear regression with Python using  plotly
# human fix:
# pip install plotly-express
# import numpy as np

import plotly.express as px

# Generate some fake data for the regression
x = [0, 1, 2, 3]
y = [1, 2, 1.5, 2.5]

# Create a scatterplot of the data
fig = px.scatter(x=x, y=y)

# Add a linear regression line to the plot
fig.add_shape(
    type="line",
    x0=0,
    y0=np.poly1d(np.polyfit(x, y, 1))(0),
    x1=3,
    y1=np.poly1d(np.polyfit(x, y, 1))(3),
    xref="x",
    yref="y",
    line=dict(color="red"),
)

# Show the plot
fig.show()
