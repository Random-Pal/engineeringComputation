import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load dataset
df = pd.read_csv('USA_cars_datasets.csv')

# Get unique brands
brands = df['brand'].unique()

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1('Price vs Year by Brand', style={'color': '#f54842', 'text-align': 'center', 'padding-top': '30px'}),

    dcc.Graph(id='scatter-plot', style={'height': '600px'}),
    html.Button("Change Brand", id="change-brand-btn", n_clicks=0, style={'margin': '20px'}),
    html.Div(id="selected-brand", style={'text-align': 'center', 'margin-top': '10px', 'font-size': '20px'})
])

# Callback to update scatter plot and display the selected brand
@app.callback(
    [Output('scatter-plot', 'figure'),
     Output('selected-brand', 'children')],
    Input('change-brand-btn', 'n_clicks')
)
def update_brand_scatter(n_clicks):
    # Cycle through the brands
    selected_brand = brands[n_clicks % len(brands)]

    # Filter data for the selected brand
    filtered_df = df[df['brand'] == selected_brand]

    # Create scatter plot
    figure = px.scatter(
        filtered_df,
        x='year',
        y='price',
        title=f'Price vs Year for {selected_brand}',
        labels={'year': 'Year', 'price': 'Price'},
        color='brand'
    )

    # Return the figure and selected brand name
    return figure, f"Selected Brand: {selected_brand}"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

