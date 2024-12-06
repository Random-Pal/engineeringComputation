import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

data = {
    'ProjectName': ['ProjectA', 'ProjectB', 'ProjectC' , 'ProjectD', 'ProjectE'],
    'Temperature': [25,28,30,22,27],
    'Pressure': [1000,950,1100,800,1050],
    'Voltage': [12, 11, 14, 10, 13],

}

engineering_projects_df = pd.DataFrame(data)

engineering_projects_df['Duration Months'] = [12, 18, 10, 25, 15]

engineering_projects_df.to_csv('engineering_sensor_readings.csv', index=False)

df = pd.read_csv('engineering_sensor_readings.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Engineering Sensor Readings Dashboard"),

    html.Label("Select Column: "),
    dcc.Dropdown(
        id ='column-dropdown',
        options=[{'label':col, 'value': col} for col in df.columns],
        value = df.columns[0]

    ),

    dcc.Graph(id='line-chart'),
])

#Define callback to update the chart based on dropdown selection
@app.callback(
    Output('line-chart', 'figure'),
    [Input('column-dropdown', 'value')]
)
def update_chart(selected_column):
    figure = {
        'data': [
            {'x': df['ProjectName'], 'y': df[selected_column], 'type': 'line', 'name': selected_column}
        ],
        'layout': {
            'title': f'{selected_column} Measurements',
            'xaxis': {'title': 'Project Name'},
            'yaxis': {'title': selected_column},
        }
    }

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)