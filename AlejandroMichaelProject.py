import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np

df = pd.read_csv('USA_cars_datasets.csv')

#brands = df['brand'].unique()

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Simple Dashboard', style={'color':'#f54842','text-align': 'center', 'padding-top': '30px'}),

    html.Label("Select Column: "),
    dcc.Dropdown(
        id='column-dropdown',
        options = [{'label':col,'value':col} for col in df.columns],
        value='Column_A',
        ##placeholder="please select an option",
        style={'width':'50%'}
    ),

    dcc.Graph(id='graph'),
    dcc.Graph(id='bar-chart',figure=px.bar(df, x='brand', y='price', title ='Sample Bar Chart')),
    dcc.Graph(id='scatter-plot',figure=px.scatter(df, x='year', y='price', title ='Sample Scatter Plot')),

    #*dcc.Dropdown(
    #  id='brand-dropdown',
    #  options=[
    #      {'label': brands, 'value': brands} for brands
    #  ],
    #),

    #dcc.Graph(
    #    id='sunburst-plot',
    #    style={'height':'600px'}

    #)

    # dcc.Graph(id='scatter-plot', style={'height': '600px'}),
    # html.Button("Change Brand", id="change-brand-btn", n_clicks=0, style={'margin': '20px'}),
    # html.Div(id="selected-brand", style={'text-align': 'center', 'margin-top': '10px', 'font-size': '20px'})

    dcc.Graph(id='pie-chart',figure=px.pie(df,values = 'price', names = 'brand', title = 'Brands sold by percentage')),



    ]

)

@app.callback(
    Output('graph', 'figure'),
    [Input('column-dropdown', 'value')],

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

# @app.callback(
#     [Output('scatter-plot', 'figureTwo'),
#     Output('selected-brand', 'children')],
#     Input('change-brand-btn', 'n_clicks')
# )
#
#
# def update_brand_scatter(n_clicks):
#     # Cycle through the brands
#     selected_brand = brands[n_clicks % len(brands)]
#
#     # Filter data for the selected brand
#     filtered_df = df[df['brand'] == selected_brand]
#
#     # Create scatter plot
#     figureTwo = px.scatter(
#         filtered_df,
#         x='year',
#         y='price',
#         title=f'Price vs Year for {selected_brand}',
#         labels={'year': 'Year', 'price': 'Price'},
#         color='blue'
#     )

#    return figureTwo

if __name__ == '__main__':
    app.run_server(debug=True)
