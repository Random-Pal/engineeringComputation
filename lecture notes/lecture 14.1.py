import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Category':['A', 'B', 'C', 'D'],
    'Values': [4, 7, 1, 3]

})

#this initilazies dash app
app = dash.Dash(__name__)

#defines layout of the app
app.layout = html.Div([
    html.H1("Simple Dashboard"),

    dcc.Slider(
        id='bar-slider',
        min=df['Values'].min(),
        max=df['Values'].max(),
        step=1,
        marks={value: str(value) for value in range(df['Values'].min(), df['Values'].max()+1)},
        value=df['Values'].min(),
    ),

    dcc.Graph(
        id='bar-chart',
        figure=px.bar(df, x='Category', y='Values', title ='Sample Bar Chart')
    )

])

@app.callback(
    Output('bar-chart', 'figure'),
    [Input('bar-slider', 'value')]
)

def update_bar_chart(selected_value):
    #filter data based on the selected value
    filtered_df = df[df['Values'] <= selected_value]

    #update bar chart
    bar_chart = px.bar(filtered_df, x='Category',y='Values', title='Sample Bar Chart')
    return bar_chart

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)