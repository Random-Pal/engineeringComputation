import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

data = {
    'Region': ['North America', 'Europe', 'Asia', 'North America', 'Europe', 'Asia'],
    'Country': ['USA', 'Germany', 'China', 'Canada', 'France', 'Japan'],
    'Sales': [50, 30, 40, 20, 25, 35],

}

df = pd.DataFrame(data)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sunburst Plot dashboard"),

    dcc.Dropdown(
        id='region-dropdown',
        options =[
            {'label':region, 'value':region} for region in df['Region'].unique()
        ],
        value='North America',
        style={'width', '50%'}
    ),

    dcc.Graph(
        id='sunburst-plot',
        style={'height':'600px'}

    )

])