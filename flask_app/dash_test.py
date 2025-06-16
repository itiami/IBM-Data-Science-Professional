import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

robotoFont = [
    "https://fonts.googleapis.com/css2?family=Roboto&display=swap"
]

def create_dash_app(server):
    dash_app = dash.Dash(__name__, server=server, url_base_pathname='/dash/', external_stylesheets=robotoFont)

    # 📊 Load dataset
    airline_data = pd.read_csv(
        'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
        encoding="ISO-8859-1",
        dtype={
            'Div1Airport': str, 'Div1TailNum': str,
            'Div2Airport': str, 'Div2TailNum': str
        })

    # 🎨 Layout with Roboto font and chart
    dash_app.layout = html.Div(
        style={'fontFamily': 'Roboto', 'padding': '20px'},
        children=[ 
            html.H1('Airline Performance Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
            html.Div([
                "Input Year: ",
                dcc.Input(id='input-year', value='2010', type='number', style={'max-width':'fit-content','padding':'5px', 'font-size': 20}),
            ], style={'font-size': 20}),
            html.Br(),
            html.Br(),
            html.Div(dcc.Graph(id='line-plot')),
        ]
    )

    # 🔁 Add callback for interactivity
    @dash_app.callback(
        Output('line-plot', 'figure'),
        Input('input-year', 'value')
    )
    def update_graph(entered_year):
        # Select data based on the entered year
        df = airline_data[airline_data['Year'] == int(entered_year)]
        
        # Group by Month and compute average arrival delay
        line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

        # Create the line chart
        fig = go.Figure(
            data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines+markers')
        )
        fig.update_layout(
            title='Average Arrival Delay per Month',
            xaxis_title='Month',
            yaxis_title='Arrival Delay (minutes)',
            template='plotly_white'
        )
        return fig

    # return dash_app
