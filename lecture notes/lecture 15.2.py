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

    html.Button('Update Chart', id='update-button', n_clicks=0),

    dcc.Graph(id='line-chart')

    ]
)

@app.callback(
    Output('line-chart','figure'),
    [Input('update-button', 'n_clicks')]
)

def update_line_chart(n_clicks):
    selected_column = np.random.choice(df.columns)

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
