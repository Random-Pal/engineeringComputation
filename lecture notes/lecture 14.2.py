import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Category':['A', 'B', 'C', 'D'],
    'Values': [4, 7, 1, 3],
    'Scores': [10, 5, 8, 2]

})

#this initilazies dash app
app = dash.Dash(__name__)

#defines layout of the app
app.layout = html.Div([
    html.H1("Multi-Graph Dashboard"),
    dcc.Graph( id='bar-chart',figure=px.bar(df, x='Category', y='Values', title ='Sample Bar Chart')),
    dcc.Graph( id='scatter-plot',figure=px.scatter(df, x='Category', y='Scores', title ='Sample Scatter Plot')),

])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)