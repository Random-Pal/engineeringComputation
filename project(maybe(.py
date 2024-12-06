import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np

df = pd.read_csv('USA_cars_datasets.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Simple Dashboard'),

    html.Label("Select Column: "),
    dcc.Dropdown(
        id='column-dropdown',
        options = [{'label':col,'value':col} for col in df.columns],
        value='Column_A',
        style={'width':'50%'}
    ),

    dcc.Graph(id='graph'),
    dcc.Graph(id='bar-chart',figure=px.bar(df, x='brand', y='price', title ='Sample Bar Chart')),
    dcc.Graph(id='scatter-plot',figure=px.scatter(df, x='year', y='price', title ='Sample Scatter Plot')),

    ]

)

@app.callback(
    Output('graph', 'figure'),
    [Input('column-dropdown', 'value')]
)
def update_chart(selected_column):
    figure = {
        'data': [
            {'x': df['year'], 'y': df[selected_column], 'type': 'line', 'name': selected_column}
        ],
        'layout': {
            'title': f'{selected_column} Measurements',
            'xaxis': {'title': 'Years'},
            'yaxis': {'title': selected_column},
        }
    }

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
