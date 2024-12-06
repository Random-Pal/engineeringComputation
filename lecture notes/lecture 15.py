import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np

np.random.seed(42)
time_index = pd.date_range('2023-01-01','2023-01-31', freq = 'D')
df = pd.DataFrame({
    'Time':time_index,
    'Column_A': np.random.rand(len(time_index)),
    'Column_B': np.random.rand(len(time_index)),
    'Column_C': np.random.rand(len(time_index)),
})

df.set_index('Time', inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Simple Dashboard'),

    dcc.Dropdown(
        id='dropdown-column',
        options = [{'label':col,'value':col} for col in df.columns],
        value='Column_A',
        style={'width':'50%'}
    ),

    dcc.Graph(id='line-chart')

    ]
)

@app.callback(
    Output('line-chart','figure'),
    [Input('dropdown-column', 'value')]
)

def update_line_chart(selected_column):
    title = selected_column + ' over Time'
    fig = {
        'data': [
            {'x': df.index, 'y':df[selected_column], 'type': 'line', 'name': selected_column}

        ],
        'layout': {
            'title': title,
            'x-axis': {'title': 'Time'},
            'y-axis': {'title': selected_column}
        }
    }
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
