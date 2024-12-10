import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the dataset
df = pd.read_csv('USA_cars_datasets.csv')

# Dictionary for state abbreviation mapping since CSV file only has full names
# and plotly likes to use to letter abbreviation for choropleth.
state_abbreviations = {
    'alabama': 'AL', 'alaska': 'AK', 'arizona': 'AZ', 'arkansas': 'AR',
    'california': 'CA', 'colorado': 'CO', 'connecticut': 'CT', 'delaware': 'DE',
    'florida': 'FL', 'georgia': 'GA', 'hawaii': 'HI', 'idaho': 'ID',
    'illinois': 'IL', 'indiana': 'IN', 'iowa': 'IA', 'kansas': 'KS',
    'kentucky': 'KY', 'louisiana': 'LA', 'maine': 'ME', 'maryland': 'MD',
    'massachusetts': 'MA', 'michigan': 'MI', 'minnesota': 'MN',
    'mississippi': 'MS', 'missouri': 'MO', 'montana': 'MT', 'nebraska': 'NE',
    'nevada': 'NV', 'new hampshire': 'NH', 'new jersey': 'NJ', 'new mexico': 'NM',
    'new york': 'NY', 'north carolina': 'NC', 'north dakota': 'ND', 'ohio': 'OH',
    'oklahoma': 'OK', 'oregon': 'OR', 'pennsylvania': 'PA', 'rhode island': 'RI',
    'south carolina': 'SC', 'south dakota': 'SD', 'tennessee': 'TN', 'texas': 'TX',
    'utah': 'UT', 'vermont': 'VT', 'virginia': 'VA', 'washington': 'WA',
    'west virginia': 'WV', 'wisconsin': 'WI', 'wyoming': 'WY'
}

# Process the dataset
df['state'] = df['state'].str.lower().map(state_abbreviations)

# Modifying dataset so that it only groups 2 columns for the dropdown & data.
brand_of_car = df.groupby('brand')['model'].count().reset_index().sort_values('model', ascending=False).head(10)
brand_of_car = brand_of_car.rename(columns={'model': 'count'}) # using model column as our total count of different brands.

top_states = df.groupby('state').size().reset_index(name='count').sort_values('count', ascending=False).head(10)

car_counts_by_state = df.groupby('state').size().reset_index(name='car_count')

# Initialize the Dash app
app = dash.Dash(__name__)

# color palette for dashboard and graphs.
color_palette = px.colors.sequential.Blues

# App layout
app.layout = html.Div([
    html.H1('US Used Car Data', style={'color': '#00509E', 'text-align': 'center'}),

    # Grid layout for graphs
    html.Div([
        # Bubble Chart
        html.Div([
            html.Label("Select Column:", style={'color': '#003F88'}),
            dcc.Dropdown(
                id='column-dropdown',
                options=[{'label': col, 'value': col} for col in ['mileage', 'price']],
                value='price',
                style={'width': '100%'}
            ),
            dcc.Graph(id='bubble-chart', style={'height': '370px'})
        ], style={'grid-column': '1 / 2'}),

        # Bar Chart with Toggle Button
        html.Div([
            html.Button(
                "Toggle Bar Chart (Brand / State)",
                id='bar-toggle-button',
                n_clicks=0,
                style={'margin-bottom': '10px', 'width': '100%', 'background-color': '#00509E', 'color': '#FFFFFF'}
            ),
            dcc.Graph(
                id='bar-chart',
                style={'height': '370px'}
            )
        ], style={'grid-column': '2 / 3'}),

        # Scatter Plot with Toggle Button
        html.Div([
            html.Button(
                "Toggle Scatter Plot (Year vs Price / Mileage vs Price)",
                id='toggle-button',
                n_clicks=0,
                style={'margin-bottom': '10px', 'width': '100%', 'background-color': '#00509E', 'color': '#FFFFFF'}
            ),
            dcc.Graph(
                id='scatter-plot',
                style={'height': '370px'}
            )
        ], style={'grid-column': '3 / 4'}),

        # Choropleth Map
        html.Div([
            dcc.Graph(
                id='choropleth-map',
                figure=px.choropleth(
                    car_counts_by_state,
                    locations='state',
                    locationmode='USA-states',
                    scope='usa',
                    color='car_count',
                    hover_name='state',
                    hover_data=['car_count'],
                    color_continuous_scale=color_palette,
                    title="Number of Cars per State"
                ),
                style={'height': '400px'}
            )
        ], style={'grid-column': '1 / 2'}),

        # Pie Chart with Toggle Button
        html.Div([
            html.Button(
                "Toggle Pie Chart (Brand / State)",
                id='pie-toggle-button',
                n_clicks=0,
                style={'margin-bottom': '10px', 'width': '100%', 'background-color': '#00509E', 'color': '#FFFFFF'}
            ),
            dcc.Graph(
                id='pie-chart',
                style={'height': '370px'}
            )
        ], style={'grid-column': '2 / 3'})

    ], style={
        'display': 'grid',
        'grid-template-columns': '1fr 1fr 1fr',  # Three columns
        'grid-gap': '20px',
        'padding': '20px',
        'background-color': '#E0F0FF'
    })
])

# Callback for bubble chart
@app.callback(
    Output('bubble-chart', 'figure'),
    [Input('column-dropdown', 'value')]
)
def update_chart(selected_column):
    figure = px.scatter(
        df,
        x='year',
        y=selected_column,
        size=selected_column,
        color=selected_column,
        title=f'Bubble Chart: Year vs {selected_column.capitalize()}',
        labels={selected_column: selected_column.capitalize()},
        color_continuous_scale=color_palette
    )
    return figure

# Callback for bar chart toggle
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('bar-toggle-button', 'n_clicks')]
)
def toggle_bar_chart(n_clicks):
    if n_clicks % 2 == 0:  # Even clicks: Show brand data
        return px.bar(
            brand_of_car,
            x='brand',
            y='count',
            color='count',
            title='Top 10 Brands by Count',
            labels={'brand': 'Brand', 'count': 'Count'},
            color_continuous_scale=color_palette
        )
    else:  # Odd clicks: Show state data
        return px.bar(
            top_states,
            x='state',
            y='count',
            color='count',
            title='Top Ten States by Count',
            labels={'state': 'State', 'count': 'Count'},
            color_continuous_scale=color_palette
        )


# Callback for scatter plot toggle
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('toggle-button', 'n_clicks')]
)
def toggle_scatter_plot(n_clicks):
    if n_clicks % 2 == 0:  # Even clicks: Year vs Price
        return px.scatter(
            df,
            x='year',
            y='price',
            title='Scatter Plot: Year vs Price',
            labels={'year': 'Year', 'price': 'Price'},
            color_continuous_scale=color_palette
        )
    else:  # Odd clicks: Mileage vs Price
        return px.scatter(
            df,
            x='mileage',
            y='price',
            title='Scatter Plot: Mileage vs Price',
            labels={'mileage': 'Mileage', 'price': 'Price'},
            color_continuous_scale=color_palette
        )


# Callback for pie chart toggle
@app.callback(
    Output('pie-chart', 'figure'),
    [Input('pie-toggle-button', 'n_clicks')]
)
def toggle_pie_chart(n_clicks):
    if n_clicks % 2 == 0:  # Even clicks: Show brand data
        return px.pie(
            brand_of_car,
            values='count',
            names='brand',
            title='Brands Sold by Percentage',
            color_discrete_sequence=color_palette
        )
    else:  # Odd clicks: Show state data
        return px.pie(
            top_states,
            values='count',
            names='state',
            title='Ten States with the Most Cars',
            color_discrete_sequence=color_palette
        )


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
